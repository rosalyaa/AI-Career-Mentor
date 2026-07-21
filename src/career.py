def recommend_career(skills):
    """
    Recommend a career based on detected skills.
    """

    skills = [skill.lower() for skill in skills]
    if (
        "python" in skills and
        "pandas" in skills and
        "numpy" in skills
    ):
        return "Data Scientist"
    elif (
        "machine learning" in skills or
        "tensorflow" in skills or
        "scikit-learn" in skills
    ):
        return "Machine Learning Engineer"
    elif (
        "html" in skills and
        "css" in skills and
        "javascript" in skills
    ):
        return "Full Stack Developer"
    elif (
        "flutter" in skills or
        "firebase" in skills
    ):
        return "Flutter Developer"
    elif (
        "opencv" in skills or
        "yolo" in skills or
        "computer vision" in skills
    ):
        return "Computer Vision Engineer"
    elif (
        "aws" in skills or
        "azure" in skills
    ):
        return "Cloud Engineer"
    else:
        return "Software Engineer"