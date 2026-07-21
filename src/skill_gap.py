CAREER_SKILLS = {

    "Data Scientist": [
        "Python",
        "Pandas",
        "NumPy",
        "Machine Learning",
        "Scikit-learn",
        "SQL",
        "TensorFlow"
    ],

    "Machine Learning Engineer": [
        "Python",
        "Machine Learning",
        "TensorFlow",
        "Scikit-learn",
        "Docker",
        "Git"
    ],

    "Full Stack Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "Python",
        "SQL",
        "Git"
    ],

    "Flutter Developer": [
        "Flutter",
        "Dart",
        "Firebase",
        "Git"
    ],

    "Computer Vision Engineer": [
        "Python",
        "OpenCV",
        "YOLO",
        "TensorFlow",
        "Machine Learning"
    ],

    "Cloud Engineer": [
        "AWS",
        "Azure",
        "Docker",
        "Linux",
        "Git"
    ],

    "Software Engineer": [
        "Python",
        "Java",
        "SQL",
        "Git",
        "GitHub"
    ]
}


def get_skill_gap(skills, career):
    """
    Returns the missing skills required
    for the recommended career.
    """

    required_skills = CAREER_SKILLS.get(career, [])

    missing = []

    user_skills = [skill.lower() for skill in skills]

    for skill in required_skills:
        if skill.lower() not in user_skills:
            missing.append(skill)

    return missing