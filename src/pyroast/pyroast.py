def roast_gpa(gpa: float) -> str:
    if gpa >= 3.9:
        return "I bet you've never known sleep before"
    elif gpa >= 3.5:
        return "I smell wasted potential"
    elif gpa >= 3.0:
        return "Are you even trying? Or is college just a networking event for you?"
    else:
        return "Your GPA is lower than my room temperature"


def roast_height(height: float) -> str:
    if height > 6.7:
        return "You might as well just be a tree!"
    elif height == 6.7:
        return "Haha funny"
    elif height >= 6.3:
        return "Too short to make it to the NBA. Almost there."
    elif height >= 6.0:
        return "Yeah, sure you are."
    elif height >= 5.8:
        return "How's the weather down there?"
    elif height >= 4.5:
        return "Willy Wonka wants you back in the cholocate factory."
    else:
        return "How is that possible?"