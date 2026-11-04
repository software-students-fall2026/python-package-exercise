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

def roast_age(age: int) -> str:
    """
    Roast the user based on their age. Takes only a whole number in years.
    Negative age is acceptable (will be considered unborn).
    """

    if not isinstance(age, int) or isinstance(age, bool):
        raise TypeError(f"Age should be a whole number of years, instead got {type(age).__name__}")

    if age > 99:
        return "Careful sandbag! Every second is a 50/50 gamble!"
    elif age > 89:
        return "Have your skin flaps grown mold yet?"
    elif age > 64:
        return "Has your family started digging your grave yet?"
    elif age > 39:
        return "We should bet on which organ starts giving up first."
    elif age > 29:
        return "Your bank account is looking pretty dry and your energy bar looks even drier."
    elif age > 19:
        return "How is the job search going? Still nothing?"
    elif age > 9:
        return "Keep eating that junk food! More joy now and more health problems later!"
    elif age > 0:
        return "You're probably a dirt eater."
    else:
        return "Did your mom's womb come with a computer?"

