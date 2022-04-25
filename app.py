from flask import Flask, request, render_template
import model

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def bpCalculate():
    if request.method == "POST":
        age = int(request.form.get("age"))
        weight = int(request.form.get("weight"))
        return render_template("home.html", bp=str(model.load(age, weight)));
    return render_template("home.html")