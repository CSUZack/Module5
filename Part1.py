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

numYears = inputValidInt("How many years of rainfall data would you like to enter? ")
rainData = []
for i in range(numYears):
    print(f"YEAR: {i+1}")
    for j in range(12):
        rainData.append(inputValidInt(f"Please enter how many inches of rainfall in month {j+1}: "))

print("RAINFALL SUMMARY")
print(f"TOTAL MONTHS: {len(rainData)}")
print(f"TOTAL RAINFALL: {sum(rainData)}")
print(f"AVERAGE RAINFALL: {sum(rainData)/ len(rainData)}")