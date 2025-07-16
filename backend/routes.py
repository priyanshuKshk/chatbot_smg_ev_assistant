from flask import Blueprint, request, jsonify
from model import ask_bot

chatbot_route = Blueprint('chatbot', __name__)

@chatbot_route.route('/ask', methods=['POST'])
def ask():
    try:
        print("Request content-type:", request.content_type)
        data = request.get_json(force=False, silent=False)
        print("Received JSON:", data)

        user_query = data.get("query", "")
        print("1")
        print(f"User query: {user_query}")
        
        response = ask_bot(user_query)
        return jsonify({"response": response})
    
    except Exception as e:
        print("❌ Error while processing request:", e)
        return jsonify({
            "error": e,
            "message": "Invalid JSON or request format"}), 400
