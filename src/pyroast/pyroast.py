def roast_gpa(gpa: float) -> str:
    if gpa >= 3.9:
        return "I bet you've never known sleep before"
    elif gpa >= 3.5:
        return "I smell wasted potential"
    elif gpa >= 3.0:
        return "Are you even trying? Or is college just a networking event for you?"
    else:
        return "Your GPA is lower than my room temperature"