from flask import Flask, render_template, request
from detection import detect_ai
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/detect",methods=['GET','POST'])
def detect():
    text= request.form.get('input_field')
    result = detect_ai(text)
    return render_template("process.html", result=result)