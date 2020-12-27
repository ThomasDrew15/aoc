#import packages
from itertools import permutations

#open input text file from AOC holding possible answers
#read each line into a list
with open("input.txt", "r") as f:
    expenses = [ int(i) for i in f ]

#declare variable with expeceted taget number set by AOC
target_number = 2020

#find pair of numbers that sum to target number, 2 refers to number of integers expected
solutions = [pair for pair in permutations(expenses, 2) if sum(pair) == target_number]
print('Solutions:', solutions)

#print 1st tuple of given solutions
print(solutions[1])

#unpack tuple into ints to * together to reach answer
int1, int2 = (solutions[1])
result = (int1 * int2 )

#print answer
print(result)

f.close()







