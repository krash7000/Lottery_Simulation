import random

upper_limit = int(input("Input upper range of lottery numbers: "))+1

range_list = list(range(1, upper_limit))
winner_list = []
combination_list = []
counter = 0

# This for loop picks the 5 winning numbers
for each in range(5):
    pick = random.choice(range_list)
    winner_list.append(pick)
    range_list.remove(pick)
winner_list.sort()

# This for loop picks the 5 combination numbers
while winner_list != combination_list:
    test_range = list(range(1, upper_limit))
    combination_list.clear()
    for each in range(5):
        pick = random.choice(test_range)
        combination_list.append(pick)
        test_range.remove(pick)
    combination_list.sort()
    print(combination_list)
    counter += 1

print(f"WINNING NUMBERS: {winner_list[0]} {winner_list[1]} {winner_list[2]} {winner_list[3]} {winner_list[4]}")
print(f"WE FOUND A MATCH: {combination_list[0]} {combination_list[1]} {combination_list[2]} {combination_list[3]} {combination_list[4]}")
print(f"This took {counter} tries!")

