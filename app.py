from flask import Flask, render_template, request, send_file
import os
import csv
from werkzeug.utils import secure_filename
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from utils.pdf_reader import extract_text
from utils.preprocessing import preprocess_text
from utils.skill_match import get_matching_skills

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

results_data = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    global results_data

    files = request.files.getlist("resume")

    if not files:
        return "Please select at least one PDF."

    job_description = request.form.get("job_description", "").strip()

    if not job_description:
        return "Please enter Job Description."

    processed_job = preprocess_text(job_description)

    results = []

    for file in files:

        if file.filename == "":
            continue

        filename = secure_filename(file.filename)

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

        file.save(filepath)

        resume_text = extract_text(filepath)

        if not resume_text.strip():
            continue

        processed_resume = preprocess_text(resume_text)

        documents = [processed_resume, processed_job]

        tfidf = TfidfVectorizer(stop_words="english")

        vectors = tfidf.fit_transform(documents)

        similarity = cosine_similarity(
            vectors[0:1],
            vectors[1:2]
        )[0][0]

        score = round(similarity * 100, 2)

        matched_skills = get_matching_skills(
            resume_text,
            job_description
        )

        results.append({
            "filename": filename,
            "score": score,
            "skills": matched_skills
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    results_data = results

    highest_score = max(
        (r["score"] for r in results),
        default=0
    )

    average_score = round(
        sum(r["score"] for r in results) / len(results),
        2
    ) if results else 0

    total_resumes = len(results)

    return render_template(
        "index.html",
        results=results,
        highest_score=highest_score,
        average_score=average_score,
        total_resumes=total_resumes
    )


@app.route("/download")
def download():

    csv_file = "results.csv"

    with open(csv_file, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Rank",
            "Resume Name",
            "Match Score",
            "Matched Skills"
        ])

        for i, result in enumerate(results_data, start=1):

            writer.writerow([
                i,
                result["filename"],
                result["score"],
                ", ".join(result["skills"])
            ])

    return send_file(csv_file, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)