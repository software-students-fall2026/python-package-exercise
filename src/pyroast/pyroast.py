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

def roast_coffee(cups: int) -> str:
    if cups < 0:
        return "Who are you trying to fool?"
    if cups == 0:
        return "No coffee? You run on pure denial."
    elif cups <= 2:
        return "Less than 2 cups? Still on the free trial of adulthood."
    elif cups <= 4:
        return "Your coffee needs a coffee."
    elif cups > 4:
        return "Your blood has turned into espresso."
    else:
        return "Are you kidding me?"
      
def roast_sleep(hours: float) -> str:
    """Roast the user based on how many hours they slept last night.

    hours must be a number between 0 and 24 inclusive.
    Raises TypeError for non-numeric input and ValueError for out-of-range values.
    """
    if isinstance(hours, bool) or not isinstance(hours, (int, float)):
        raise TypeError(f"hours must be a number, got {type(hours).__name__}")
    if hours < 0 or hours > 24:
        raise ValueError(f"hours must be between 0 and 24, got {hours}")

    if hours == 0:
        return "Zero hours? Your eye bags have eye bags."
    elif hours < 4:
        return "That's not sleep, that's a long blink."
    elif hours < 6:
        return "Running on vibes and caffeine, I see."
    elif hours < 8:
        return "Almost a functional adult. Almost."
    elif hours <= 10:
        return "Eight hours? Who are you, a wellness influencer?"
    else:
        return "You're not well-rested, you're hibernating."
