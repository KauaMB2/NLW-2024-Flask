from src.main.server.server import app
from src.models.settings.db_connection_handler import db_connection_handler
from flask_cors import CORS
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})# Initialize CORS and allow requests from http://localhost:5173

if __name__ == "__main__":
    db_connection_handler.connect()# Connect to the database
    app.run(host="0.0.0.0", port=3000, debug=True)