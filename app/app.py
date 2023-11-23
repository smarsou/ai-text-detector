from flask import Flask, render_template, request, jsonify
import detection

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/process",methods=['POST'])
def process():
    data = request.form.get('data')
    result = detection.detect_ai(data)
    return jsonify({'int': result})
