#open input text file from AOC holding possible answers
#read each line into a list
with open("passes.txt", "r") as f:
    pswds = [ str(i) for i in f ]

string = pswds[0]

    #split strong by whitepsace
stringsplit = string.split()
print(stringsplit)

    #create substring of letter
substring = stringsplit[1]
print(substring[0])

    #count how often substring letter appears in password
count =stringsplit[2].count(substring[0])
print(count)


    #get parameters for how often letter should appear
countValues = stringsplit[0]
print(countValues)

    #split values with - delimter
splitCountValues = countValues.split("-")
print(splitCountValues)

    #assign values to variables
lowValue = int(splitCountValues[0])
highValue = int(splitCountValues[1])
print(lowValue, "and", highValue)


def validCheck(count, lowValue, highValue):
        #if/else statement to decide if password valid
        #password is valid if letter is counted between low and high values
    if count >= highValue or count <= lowValue:
        print("password not valid")
    else:
        print("password valid")

validCheck(count, lowValue, highValue)