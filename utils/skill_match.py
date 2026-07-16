import re

COMMON_SKILLS = [
    "python",
    "java",
    "c++",
    "c",
    "javascript",
    "html",
    "css",
    "sql",
    "mysql",
    "mongodb",
    "flask",
    "django",
    "react",
    "node",
    "git",
    "github",
    "aws",
    "docker",
    "machine learning",
    "deep learning",
    "nlp",
    "tensorflow",
    "pandas",
    "numpy",
    "power bi",
    "excel"
]


def get_matching_skills(resume_text, job_description):
    resume = resume_text.lower()
    job = job_description.lower()

    matched = []

    for skill in COMMON_SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, resume) and re.search(pattern, job):
            matched.append(skill.title())

    return matched