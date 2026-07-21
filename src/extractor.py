import re

# Common technical skills
SKILLS_DB = [
    "Python",
    "Java",
    "C",
    "C++",
    "HTML",
    "CSS",
    "JavaScript",
    "SQL",
    "MySQL",
    "MongoDB",
    "Firebase",
    "Flutter",
    "Dart",
    "Git",
    "GitHub",
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "Data Science",
    "TensorFlow",
    "Keras",
    "PyTorch",
    "OpenCV",
    "Scikit-learn",
    "Pandas",
    "NumPy",
    "Power BI",
    "Tableau",
    "Excel",
    "AWS",
    "Azure",
    "Docker",
    "Linux",
    "FastAPI",
    "Flask",
    "Django",
    "Streamlit",
    "YOLO",
    "Computer Vision"
]


def extract_email(text):
    """
    Extract email from resume.
    """
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_phone(text):
    """
    Extract phone number.
    """
    pattern = r"(?:\+91[- ]?)?[6-9]\d{9}"
    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_skills(text):
    """
    Extract skills from resume.
    """
    found_skills = []

    text = text.lower()

    for skill in SKILLS_DB:
        if skill.lower() in text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))