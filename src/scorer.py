def calculate_score(text):
    """
    Calculate resume score and provide suggestions.
    """

    score = 100
    feedback = []

    text = text.lower()

    sections = {
        "education": 10,
        "skills": 10,
        "project": 15,
        "experience": 15,
        "certification": 10,
        "internship": 10,
        "achievement": 10,
        "objective": 5,
        "summary": 5,
        "contact": 10
    }

    for section, marks in sections.items():
        if section not in text:
            score -= marks
            feedback.append(f"Add a '{section.title()}' section.")
    score = max(score, 0)

    return score, feedback


def resume_feedback(score):
    """
    Returns overall feedback based on score.
    """

    if score >= 90:
        return "🟢 Excellent Resume"

    elif score >= 75:
        return "🟡 Good Resume"

    elif score >= 60:
        return "🟠 Average Resume"

    else:
        return "🔴 Needs Improvement"