from itertools import permutations

with open("input.txt", "r") as f:
    expenses = [ int(i) for i in f ]

numbers = expenses
target_number = 2020

solutions = [pair for pair in permutations(numbers, 3) if sum(pair) == target_number]
print('Solutions:', solutions)

print(solutions[1])

int1, int2, int3 = (solutions[1])
result = (int1 * int2 * int3)

print(result)









