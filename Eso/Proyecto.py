from re import template
from flask import Flask,  render_template;

app = Flask(__name__)

@app.route("/")
def Mostrar():
    return render_template('index.html')

app.run(debug=True)