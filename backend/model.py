import os
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import google.generativeai as genai
from dotenv import load_dotenv
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("GOOGLE_API_KEY")

if API_KEY:
    
    os.environ["GOOGLE_API_KEY"] = API_KEY
    import google.generativeai as genai
    genai.configure(api_key=API_KEY)
    print("✅ GOOGLE_API_KEY loaded successfully.")
else:
    raise Exception("❌ GOOGLE_API_KEY not found! Please check your .env file.")

gemini_model = genai.GenerativeModel("gemini-1.5-pro-latest")

# Load multiple CSVs
DATASET_FOLDER = os.path.join(os.path.dirname(__file__) ,"dataset")
csv_files = ["company_info.csv", "Data[1].csv","dataset.csv","ev_service_data.csv" ,"products.csv"
]  # Add new CSV filenames here

text_data = []

for file in csv_files:
    file_path = os.path.join(DATASET_FOLDER, file)
    try:
        df = pd.read_csv(file_path, on_bad_lines='warn')  # Ignore bad lines gracefully
        cleaned_text = [" | ".join(row.dropna().astype(str)) for _, row in df.iterrows()]
        text_data.extend(cleaned_text)
        print(f"Loaded {file} with {len(cleaned_text)} rows")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except pd.errors.ParserError as pe:
        print(f"Parser error in {file}: {pe}")
    except Exception as e:
        print(f"Unexpected error loading {file}: {e}")


# Create embeddings from combined data
model = SentenceTransformer('all-MiniLM-L6-v2')
corpus_embeddings = model.encode(text_data, show_progress_bar=True)

def ask_bot(user_query):
    # Normalize query for matching
    
    normalized_query = user_query.strip().lower()
    print(f"Normalized query: {normalized_query}")

    # Custom hardcoded replies
    identity_questions = [
        "who are you", "what is your name", "tell me about yourself", "introduce yourself"
    ]
    if normalized_query in identity_questions:
        return "I am SMG-EV Assistant. I provide information about our website, services, and products to help you learn more about us."
    comapny_questions = [
        "for whom you are working for", "what is your company name", "tell me comapny name", "about your comapany"
    ]
    if normalized_query in comapny_questions:
        return "SMG Electric Vehicles,A leading provider of electric vehicle fluids, greases, and related support services across India."


def ask_bot(user_query):
    try:
        # Generate embedding for user query
        query_embedding = model.encode([user_query])
        similarities = cosine_similarity(query_embedding, corpus_embeddings)[0]
        top_indices = similarities.argsort()[-3:][::-1]

        matched_context = "\n".join([text_data[i] for i in top_indices])
        
        prompt = f"""
You are a helpful chatbot named SMG-EV Assistant. Answer the user's question clearly and professionally.

Context:
{matched_context}

User Question:
{user_query}

Answer:
"""

        print("Sending prompt to Gemini...")
        response = gemini_model.generate_content(prompt)
        print("Gemini response received")
        return response.text.strip()
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"Gemini API Error: {e}")
        return "Sorry, something went wrong while trying to answer your question."
