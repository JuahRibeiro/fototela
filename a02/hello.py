clcfrom flask import Flask, render_template
app = Flask(__name__)


#decorator
@app.route("/")
def homepage():
    return "hello Web.py"
@app.route("/start")
def start():
    return "starting..."
@app.route("/teste")
def Lista_usuario():
    return render_template ("teste.html")
app.run(debug=True)