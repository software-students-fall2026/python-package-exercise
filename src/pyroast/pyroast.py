def roast_gpa(gpa: float) -> str:
    if isinstance(gpa, bool) or not isinstance(gpa, (int, float)):
        raise TypeError(f"gpa must be a number, got {type(gpa).__name__}")

    if gpa < 0 or gpa > 4.0:
        raise ValueError(f"gpa must be between 0 and 4.0, got {gpa}")

    if gpa >= 3.9:
        return "I bet you've never known sleep before"
    elif gpa >= 3.5:
        return "I smell wasted potential"
    elif gpa >= 3.0:
        return "Are you even trying? Or is college just a networking event for you?"
    elif gpa >=2.5:
        return "At this point, it might be better to give up"
    elif gpa >=2.0:
        return "I see you gave up, smartest choice you've ever made"
    else:
        return "Your GPA is lower than my room temperature"


def roast_height(height: float) -> str:
    """Roast the user based on their height in feet.

    height must be a number between 1 and 9 inclusive.
    Raises TypeError for non-numeric input and ValueError for out-of-range values.
    """
    if isinstance(height, bool) or not isinstance(height, (int, float)):
        raise TypeError(f"height must be a number, got {type(height).__name__}")
    if height < 1 or height > 9:
        raise ValueError(f"height must be between 1 and 9 feet, got {height}")

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
    """Roast the user based on how many cups of coffee they drink a day.

    cups must be a whole number of 0 or more.
    Raises TypeError for non-integer input and ValueError for negative values.
    """
    if isinstance(cups, bool) or not isinstance(cups, int):
        raise TypeError(f"cups must be a whole number, got {type(cups).__name__}")
    if cups < 0:
        raise ValueError(f"cups cannot be negative, got {cups}")

    if cups == 0:
        return "No coffee? You run on pure denial."
    elif cups <= 2:
        return "Less than 2 cups? Still on the free trial of adulthood."
    elif cups <= 4:
        return "Your coffee needs a coffee."
    else:
        return "Your blood has turned into espresso."


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
    elif age > 31:
        return "Your bank account is looking pretty dry and your energy bar looks even drier."
    elif age > 27:
        return "Everyone else already has kids, a car, and a house... what are you still doing in your mom's basement?"
    elif age > 24:
        return "Quarter-life crisis mode: fully engaged."
    elif age > 19:
        return "How is the job search going? Still nothing?"
    elif age > 9:
        return "Keep eating that junk food! More joy now and more health problems later!"
    elif age > 0:
        return "You're probably a dirt eater."
    else:
        return "Did your mom's womb come with a computer?"

