from flask import Flask, render_template, request, jsonify
from detection import detect_ai
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/process",methods=['POST'])
def process():
    data = request.form.get('data')
    result = detect_ai(data)
    return jsonify({'int': 75})