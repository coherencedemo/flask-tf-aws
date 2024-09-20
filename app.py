import os
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis_client = Redis(host=os.environ['REDIS_HOST'], port=6379)

@app.route('/')
def hello():
    visits = redis_client.incr('visits')
    return f'Hello! I have been seen {visits} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)