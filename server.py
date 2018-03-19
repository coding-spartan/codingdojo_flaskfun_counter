from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route("/")
def index():
    if not session.get("count"):
        session["count"] = 0
    #The above lines are there to make sure the count starts at zero    
    session["count"] += 1
    return render_template("index.html", count=session["count"])

@app.route("/reloadplus2", methods=["POST"])
def reloadplus2():
    session["count"] += 1
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    session["count"] = 0
    return redirect("/")

app.run(debug=True)
