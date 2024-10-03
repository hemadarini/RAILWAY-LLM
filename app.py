from flask import Flask, render_template, request, jsonify
import google.generativeai as gemini

app = Flask(__name__)

# Configure the Gemini API with your API key
gemini.configure(api_key='AIzaSyDTOaHGeeO2gQJfZizcpUITiC7ORToamok')

# Initialize the model
model = gemini.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(user_message):
    chat = model.start_chat()
    response = chat.send_message(user_message)
    return response.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['message']
    chatbot_response = get_gemini_response(user_message)
    return jsonify({'response': chatbot_response})

if __name__ == '__main__':
    app.run(debug=True)
