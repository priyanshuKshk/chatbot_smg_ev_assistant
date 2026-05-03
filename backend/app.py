from flask import Flask, send_from_directory
from flask_cors import CORS
from routes import chatbot_route
from model import ask_bot
import os
app = Flask(__name__)

CORS(app)

# Register Blueprint for chatbot API
app.register_blueprint(chatbot_route)

@app.route("/")
def home():
    return {"message": "Backend running"}

# if __name__ == "__main__":
#     app.run(debug=True)

# if __name__ == "__main__":
#     app.run(debug=False, host="0.0.0.0", port=5000)

if __name__ == "__main__":
    if os.environ.get("FLASK_ENV") == "production":
        app.run(debug=False, host="0.0.0.0", port=5000)
    else:
        app.run(debug=True, host="0.0.0.0", port=5000)