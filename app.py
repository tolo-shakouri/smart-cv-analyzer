from flask import Flask, render_template, request
from parser import extract_text_from_pdf, find_skills

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    skills = []

    if request.method == "POST":
        pdf_file = request.files.get("resume")

        if pdf_file:
            text = extract_text_from_pdf(pdf_file)
            skills = find_skills(text)

    return render_template("index.html", skills=skills)


if __name__ == "__main__":
    app.run(debug=True)
