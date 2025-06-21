from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", current_year=datetime.utcnow().year)

@app.route("/projects")
def projects():
    return render_template("projects.html", current_year=datetime.utcnow().year)

@app.route("/about")
def about():
    return render_template("about.html", current_year=datetime.utcnow().year)

@app.route("/contact")
def contact():
    return render_template("contact.html", current_year=datetime.utcnow().year)

if __name__ == "__main__":
    app.run(debug=True)