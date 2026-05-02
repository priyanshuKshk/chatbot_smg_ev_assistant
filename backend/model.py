import os
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import google.generativeai as genai

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise Exception("GOOGLE_API_KEY not found! Set it in Render environment.")

genai.configure(api_key=API_KEY)
gemini_model = genai.GenerativeModel("gemini-3-flash-preview")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_FOLDER = os.path.join(BASE_DIR, "dataset")

csv_files = [
    "company_info.csv",
    "Data[1].csv",
    "dataset.csv",
    "ev_service_data.csv",
    "products.csv"
]

text_data = []

for file in csv_files:
    file_path = os.path.join(DATASET_FOLDER, file)
    print("Trying to load:", file_path)

    try:
        df = pd.read_csv(file_path, on_bad_lines='warn')
        cleaned_text = [
            " | ".join(row.dropna().astype(str))
            for _, row in df.iterrows()
        ]

        text_data.extend(cleaned_text)
        print(f"✅ Loaded {file} with {len(cleaned_text)} rows")

    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")

    except Exception as e:
        print(f"❌ Error loading {file}: {e}")

print("Total data loaded:", len(text_data))

model = SentenceTransformer('all-MiniLM-L6-v2')

if len(text_data) > 0:
    corpus_embeddings = model.encode(text_data, show_progress_bar=True)
else:
    corpus_embeddings = []
    print("⚠️ No data loaded, embeddings empty")


def ask_bot(user_query):
    try:
        # Safety check
        if len(corpus_embeddings) == 0:
            return "No data available. Please check dataset loading."

        # Normalize query
        normalized_query = user_query.strip().lower()

        # -------------------------------
        # 💬 CUSTOM RESPONSES
        # -------------------------------
        if normalized_query in [
            "who are you", "what is your name",
            "tell me about yourself", "introduce yourself"
        ]:
            return "I am SMG-EV Assistant. I provide information about our website, services, and products."

        if normalized_query in [
            "company name", "your company", "who you work for"
        ]:
            return "SMG Electric Vehicles, a provider of EV fluids, greases, and services in India."

        # -------------------------------
        # 🔍 EMBEDDING SEARCH
        # -------------------------------
        query_embedding = model.encode([user_query])

        similarities = cosine_similarity(query_embedding, corpus_embeddings)[0]
        top_indices = similarities.argsort()[-3:][::-1]

        matched_context = "\n".join([text_data[i] for i in top_indices])

        # -------------------------------
        # 🧠 GEMINI PROMPT
        # -------------------------------
        prompt = f"""
You are SMG-EV Assistant. Answer clearly and professionally.

Context:
{matched_context}

User Question:
{user_query}

Answer:
"""

        print("🚀 Sending to Gemini...")
        response = gemini_model.generate_content(prompt)

        return response.text.strip()

    except Exception as e:
        import traceback
        traceback.print_exc()
        print("❌ ERROR:", e)
        return "Sorry, something went wrong while trying to answer your question."