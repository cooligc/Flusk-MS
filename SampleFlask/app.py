from flask import Flask, request
app = Flask(__name__)

@app.route('/hey')
def hello():
    return "Hello ! Sitakant"

@app.route('/health')
def health():
    return "I am healthy",200

if __name__ == "__main__":
    app.run(host='0.0.0.0',threaded=True)