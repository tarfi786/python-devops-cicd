from flask import Flask, render_template

app = Flask(__name__)

# -----------------------------
# Home
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# About
# -----------------------------
@app.route("/about")
def about():
    return render_template("about.html")


# -----------------------------
# Projects
# -----------------------------
@app.route("/projects")
def projects():
    return render_template("projects.html")


# -----------------------------
# Contact
# -----------------------------
@app.route("/contact")
def contact():
    return render_template("contact.html")


# -----------------------------
# Health Check
# -----------------------------
@app.route("/health")
def health():
    return {"status": "UP"}


# -----------------------------
# Version
# -----------------------------
@app.route("/version")
def version():
    return {"version": "1.0.0"}


# -----------------------------
# Custom 404 Page
# -----------------------------
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
