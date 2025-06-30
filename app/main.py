from flask import Flask, request
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
request_counter = Counter('http_requests_total', 'Total API Requests')

@app.route('/')
def home():
    return "Welcome to the API. Use the /api endpoint."
    
@app.route('/api', methods=['GET', 'POST'])
def api():
    request_counter.inc()
    headers = dict(request.headers)
    method = request.method
    body = request.get_json(force=True, silent=True)

    return {
        "message": "Welcome to our demo API, here are the details of your request:",
        "headers": headers,
        "method": method,
        "body": body
    }

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
