from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World! This is a simple AWS app."

@app.route('/env')
def environment():
    return f"The environment name is: {os.environ.get('ENVIRONMENT_NAME', 'not set')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))