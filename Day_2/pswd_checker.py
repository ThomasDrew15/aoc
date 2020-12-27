#open input text file from AOC holding possible answers
#read each line into a list
with open("inputd2.txt", "r") as f:
    pswds = [ int(i) for i in f ]

print(pswds[0])