#recursive function to ask for a valid integer and to ask for a retry on any value error
def inputValidInt(prompt, retries=5):
    if retries <= 0:
        print("Too many failures in user input, aborting.\n")
        exit()
    try:
        return int(input(prompt))
    except ValueError:
        print("Something was wrong with that input, please try again.\n")
        retries -=1
        return inputValidInt(prompt, retries)

numBooks = inputValidInt("How many books did you purchase this month?")

points = 0
if numBooks >= 2 and numBooks < 4:
    points = 5
elif numBooks >= 4 and numBooks < 6:
    points = 15
elif numBooks >= 6 and numBooks < 8:
    points = 30
elif numBooks >= 8:
    points = 60

print(f"You've earned {points} points!")
    