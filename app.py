from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Initialize an empty list to store chat messages
chat_history = []

@app.route('/')
def index():
    return render_template('index.html', chat_history=chat_history)

@app.route('/send_message', methods=['POST'])
def send_message():
    # Get the user message from the form data
    user_message = request.form['message']

    # Create a new chat message dict with the user message and AI response
    chat_message = {
        'speaker': 'player',
        'text': user_message
    }

    # Get the current chat transcript from the session
    chat_transcript = session.get('chat_transcript', [])

    # Append the new chat message to the transcript
    chat_transcript.append(chat_message)

    # Update the chat transcript in the session
    session['chat_transcript'] = chat_transcript

    # Render the chat message HTML template with the chat message data
    return render_template('chat_message.html', message=chat_message)

if __name__ == '__main__':
    app.run(debug=True)