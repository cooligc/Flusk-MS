from flask import Flask, request, redirect, url_for,abort
app = Flask(__name__)

@app.route('/hey')
def hello():
    return "Hello ! Sitakant"

@app.route('/health')
def health():
    return "I am healthy",200

@app.route('/name/<name>')
def printPath(name):
    if name == 'sitakant':
        return redirect (url_for('hello'))
    else:
        abort(401)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=7878,threaded=True,debug=True)