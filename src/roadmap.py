ROADMAPS = {

    "Data Scientist": [
        "Python Programming",
        "Statistics & Probability",
        "NumPy & Pandas",
        "Data Visualization",
        "Machine Learning",
        "Deep Learning",
        "SQL",
        "Projects & Kaggle"
    ],

    "Machine Learning Engineer": [
        "Python",
        "Linear Algebra",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow / PyTorch",
        "Computer Vision",
        "Model Deployment",
        "Docker & Git"
    ],

    "Full Stack Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Python / Node.js",
        "SQL",
        "REST APIs",
        "Deployment"
    ],

    "Flutter Developer": [
        "Dart",
        "Flutter Widgets",
        "State Management",
        "Firebase",
        "REST API",
        "Authentication",
        "Play Store Deployment",
        "Projects"
    ],

    "Computer Vision Engineer": [
        "Python",
        "OpenCV",
        "Image Processing",
        "YOLO",
        "TensorFlow",
        "Object Detection",
        "Model Deployment",
        "Projects"
    ],

    "Cloud Engineer": [
        "Linux",
        "Networking",
        "AWS",
        "Azure",
        "Docker",
        "Kubernetes",
        "CI/CD",
        "Cloud Projects"
    ],

    "Software Engineer": [
        "Programming",
        "Data Structures",
        "Algorithms",
        "OOP",
        "SQL",
        "Git & GitHub",
        "Projects",
        "Interview Preparation"
    ]
}


def generate_roadmap(career):
    """
    Returns the learning roadmap
    for the recommended career.
    """

    return ROADMAPS.get(
        career,
        ["Start learning programming."]
    )