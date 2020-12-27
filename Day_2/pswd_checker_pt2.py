#open input text file from AOC holding possible answers
#read each line into a list
#with open("test_strings.txt", "r") as f:
with open("passes.txt", "r") as f:
    pswds = [ str(i) for i in f ]


validPasswords = 0
repeats = 0
notInString = 0
errors = 0


for i in pswds:
    string = str(i)
    #print(string)


        #split strong by whitepsace
    stringsplit = string.split()
#print(stringsplit, "split string")

        #create substring of letter
    substring = stringsplit[1]
#print(substring[0])



        #create substring, letter only
    keyLetter = substring[0]
#print(keyLetter)

        #create string from stringSplit[2]
    keyString = stringsplit[2]
#print(keyString)



        #count how often substring letter appears in password
    count =stringsplit[2].count(substring[0])
#print(count, "count of how often letter appears")



        #get parameters for how often letter should appear
    countValues = stringsplit[0]
#print(countValues)

        #split values with - delimter
    splitCountValues = countValues.split("-")
#print(splitCountValues)

        #assign values to variables
    lowValue = int(splitCountValues[0])
    highValue = int(splitCountValues[1])
    print("values are ", lowValue, "and", highValue)

        #show what indexes are relevant 
    print(keyString, "is the key string")
    print(keyLetter, "is the key letter")

        #get charater at first index value
    indexValueLow = keyString[lowValue -1]
    print(indexValueLow, "low value index")

        #get character at second index value
    indexValueHigh = keyString[highValue -1]
    print(indexValueHigh, "high value index")

        #if the key letter is not present in the string, finish
    if keyLetter not in keyString:
        print("not in string")
        notInString +=1
        continue
    else:
            #if the character at both index values is the same, finish
        if indexValueLow == indexValueHigh:
            print("cannot repeat at both indexes")
            repeats +=1
            continue
        else:
            if indexValueHigh == keyLetter or indexValueLow == keyLetter:
                #passes
                print("pass")
                validPasswords +=1

print(validPasswords, "valid passwords...", repeats, "repeats...", notInString, "not in string...")


    
            