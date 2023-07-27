import random

def roll_dice():
    return random.randint(1, 6)

def play_craps():
    # Initial roll
    dice1 = roll_dice()
    dice2 = roll_dice()
    roll_sum = dice1 + dice2
    print(f"You rolled {dice1} + {dice2} = {roll_sum}")

    if roll_sum in [2, 3, 12]:
        print("You lose")
    elif roll_sum in [7, 11]:
        print("You win")
    else:
        print("Point is", roll_sum)
        point = roll_sum
        while True:
            dice1 = roll_dice()
            dice2 = roll_dice()
            roll_sum = dice1 + dice2
            print(f"You rolled {dice1} + {dice2} = {roll_sum}")
            if roll_sum == 7:
                print("You lose")
                break
            elif roll_sum == point:
                print("You win")
                break

play_craps()


"""
# Q3: 
def duplicates(lst):
    return list(set(lst))

# Test 
numbers = input("Enter ten numbers: ").split()
numbers = [int(num) for num in numbers]

distinct_num = duplicates(numbers)

print("The distinct numbers are:", ' '.join(map(str, distinct_num)))


    
"""
"""
# Q2
def index_of_smallest_element(lst):
    min_index = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[min_index]:
            min_index = i
    return min_index

# Test 
numbers = []
for _ in range(10):
    number = int(input("Enter a number: "))
    numbers.append(number)

smallest_index = index_of_smallest_element(numbers)
print("Index of the smallest element:", smallest_index)

"""