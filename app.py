from flask import Flask, request, jsonify
from cloudant_helper import create_booking, get_all_bookings
from ai_assistant import create_session, send_message_to_assistant

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to AI-Powered Airline Management System by Ajay Puniparthi!"

@app.route('/book', methods=['POST'])
def book_flight():
    data = request.json
    response = create_booking(data)
    return jsonify(response)

@app.route('/bookings', methods=['GET'])
def list_bookings():
    bookings = get_all_bookings()
    return jsonify(bookings)

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get('message')
    session_id = create_session()
    ai_response = send_message_to_assistant(message, session_id)
    return jsonify(ai_response)

if __name__ == '__main__':
    app.run(debug=True)