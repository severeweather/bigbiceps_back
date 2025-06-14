from datetime import datetime, date

ACTIVITY_LEVELS = {
    "sed": 1.2,
    "lig": 1.375,
    "mod": 1.55,
    "ver": 1.725,
    "ext": 1.9,
}

GOALS = {
    "losew": -500,
    "gainw": 500,
    "mainw": 0,
    "gainm": 250,
    "mainm": 0,
}

def calculateBMR(weight, height, sex, date_of_birth):
    date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
    age = date.today().year - date_of_birth.year

    if sex == 'm':
        return 10 * weight + 6.25 * height - 5 * age + 5
    elif sex == 'f':
        return 10 * weight + 6.25 * height - 5 * age - 161
    return 0

def calculateTDEE(bmr, activity_level):
    if activity_level not in ACTIVITY_LEVELS:
        return
    return bmr * ACTIVITY_LEVELS[activity_level]

def adjustTDEE(tdee, goal):
    if goal not in GOALS:
        return
    return tdee + GOALS[goal]

def calculate_macros_intake(user):
    BMR = calculateBMR(
        user.weight, user.height,
        user.sex, str(user.date_of_birth)
        )
    
    TDEE = calculateTDEE(BMR, user.activity_level)
    TDEE = adjustTDEE(TDEE, user.goal)

    return {
        "calories": int(TDEE),
        "protein": int(user.weight * 2.0),
        "fats": int(TDEE * 0.25 / 9),
        "carbs": int((TDEE - (TDEE * 0.25) - (user.weight * 2.0 * 4)) / 4),
    }
