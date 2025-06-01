from flask import Flask, render_template, request, jsonify, session
from claude_api import ClaudeAPI
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-here')

claude_api = ClaudeAPI()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if 'conversation' not in session:
            session['conversation'] = []
        
        response = claude_api.send_message(user_message, session['conversation'])
        
        session['conversation'].extend([
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": response}
        ])
        
        session.modified = True
        
        return jsonify({
            'response': response,
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({
            'response': f'Error: {str(e)}',
            'status': 'error'
        }), 500

@app.route('/clear', methods=['POST'])
def clear_conversation():
    session.pop('conversation', None)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)