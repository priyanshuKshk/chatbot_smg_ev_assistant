
# 🤖 SMG EV Chatbot Assistant

An AI-powered chatbot designed for **SMG Electric Vehicles** to answer user queries about products, services, insurance, and company information using structured data and Gemini AI.

---

##  Features

*  AI-powered chatbot using Gemini API
*  Uses structured JSON & CSV datasets for accurate responses
*  Fast backend with Flask
*  Interactive frontend built with React + Tailwind CSS
*  Context-aware responses based on company data
*  Modular and scalable backend structure

---

## 🛠️ Tech Stack

### Frontend

* React.js
* Tailwind CSS
* Framer Motion

### Backend

* Flask (Python)
* Google Gemini API (`google-genai`)
* Pandas (for CSV handling)

### Data Sources

* JSON files (company info, services, policies)
* CSV datasets (products, services, etc.)

---

##  Project Structure

```
chatbot_smg_ev_assistant/
│
├── frontend/                # React frontend
│
├── backend/
│   ├── app.py              # Flask server
│   ├── model.py            # Gemini logic
│   ├── dataset/            # JSON & CSV files
│   └── .env                # API keys
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/chatbot_smg_ev_assistant.git
cd chatbot_smg_ev_assistant
```

---

### 2️⃣ Setup Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

---

### 3️⃣ Add Environment Variables

Create a `.env` file inside `/backend`:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

### 4️⃣ Run Backend

```bash
python app.py
```

Server runs at:

```
http://127.0.0.1:5000
```

---

### 5️⃣ Setup Frontend

```bash
cd frontend
npm install
npm start
```

---

##  How It Works

1. User sends query from the frontend
2. Flask backend receives request (`/ask`)
3. Backend combines:

   * User query
   * JSON/CSV context data
4. Sends structured prompt to Gemini
5. Gemini generates a response
6. Response is returned to the frontend

---

## 🧪 Example Query

```
User: What is the price of the SMG scooter?
Bot: The SMG electric scooter starts from ₹XX, XXX depending on the model...
```

---

##  Common Issues

###  API Key Error

* Ensure `.env` is loaded properly
* Check the key from Google MakerSuite

###  Model Not Found

* Use:

```
models/gemini-1.5-flash-latest
```

###  CSV Errors

* Ensure consistent columns
* Remove malformed rows

---

## 🔮 Future Improvements

* Admin dashboard for managing chatbot data
* Better prompt engineering
* Database integration (MongoDB/MySQL)
* Multi-language support
* Deployment (Render / Vercel)

---

##  Author

**Priyanshu Kaushik**

* B.E. CSE, UIET Chandigarh
* GitHub: https://github.com/priyanshuKshk

---

##  License

This project is for educational and development purposes.

---

##  Contribute

Feel free to fork and improve this project!

---
