from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get("APP_KEY")

messages = []


@app.route('/')
def index():
    return render_template('index.html', current_year=datetime.now().year)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        messages.append({
            'name': name,
            'email': email,
            'message': message,
            'timestamp': datetime.now().isoformat()
        })

        return jsonify({'success': True, 'message': 'Thank you for your message!'})
    
    return render_template('contact.html')

@app.route('/api/messages')
def get_messages():
    return jsonify(messages)

@app.route('/api/health')
def health_check()
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
