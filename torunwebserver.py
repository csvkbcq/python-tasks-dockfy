from torunwebserver import Flask, jsonify
app = Flask(__name__)
@app.route('/')
def home():
    return "Welcome to the Simple Flask Web Server!"
@app.route('/data')
def data():
    return jsonify({"message": "Hello, World!", "status": "success"})
@app.route('/hello/<name>')
def hello_name(name):
    return f"Hello, {name}!"
if __name__ == '__main__':
    app.run(debug=True)


    
#it works with use of separate folder creation and pip installing flask 