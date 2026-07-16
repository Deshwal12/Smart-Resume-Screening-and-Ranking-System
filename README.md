# AI Resume Screening & Candidate Ranking System

## Project Description

This project is an AI-based Resume Screening and Candidate Ranking System developed using Python, Flask, NLP, and Machine Learning.

The system extracts text from PDF resumes, preprocesses the text, compares it with a Job Description using TF-IDF Vectorization and Cosine Similarity, and ranks candidates based on their similarity score.

---

## Features

- Upload Multiple Resume PDFs
- Enter Job Description
- Extract Text from PDF Resumes
- NLP Preprocessing
- TF-IDF Vectorization
- Cosine Similarity
- Candidate Ranking
- Top Matching Skills
- Highest Score
- Average Score
- Total Resumes Uploaded
- Download Results as CSV

---

## Technologies Used

- Python
- Flask
- HTML
- CSS
- PDFPlumber
- Scikit-learn
- NLP
- TF-IDF
- Cosine Similarity

---

## Folder Structure

```
AI-Resume-Screening/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── uploads/
├── templates/
├── static/
└── utils/
```

---
## Screenshots

### Home Page
![Home Page](screenshots/home_page.png)

### Candidate Ranking
![Candidate Ranking](screenshots/candidate_ranking.png)

### CSV Results
![CSV Results](screenshots/csv_result.png)

## How to Run

1. Install the dependencies

```
pip install -r requirements.txt
```

2. Run the project

```
python app.py
```

3. Open

```
http://127.0.0.1:5000
```

---

## Author

Jyoti 