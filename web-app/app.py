from flask import Flask, render_template, request, jsonify
import detection

app = Flask(__name__)
proxy_url_path="/lab/hackaton"

@app.route(proxy_url_path)
def index():
    return render_template('index.html', proxy_url_path=proxy_url_path)

@app.route(proxy_url_path + "/process",methods=['POST'])
def process():
    data = request.form.get('data')
    result = detection.detect_ai(data)
    return jsonify({'int': result})
