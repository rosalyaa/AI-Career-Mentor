def get_resume_status(score):
    """
    Return the resume status based on the score.
    """

    if score >= 90:
        return "🟢 Excellent"

    elif score >= 75:
        return "🟡 Good"

    elif score >= 60:
        return "🟠 Average"

    else:
        return "🔴 Needs Improvement"