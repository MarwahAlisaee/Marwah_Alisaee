# Suppose that the tuition for a university is $10,000 this year and increases 5% every year. In
# one year, the tuition will be $10,500. Write a program that computes the tuition in ten years
# and the total cost of four years’ worth of tuition after the tenth year
"""
for i in range(8):
    for j in range(8-i):
        print(" ", end=" ")
    for k in range(2 ** i):
        print(format(2 ** k, "2d"), end=" ")
    for l in range(2 ** (i - 1), 0, -1):
        print(format(l, "2d"), end=" ")
    print()
    """



for i in range(8):
    for j in range(8 - i):
        print("    ", end="")
    
    num = 1
    for j in range(i + 1):
        print(format(num, "3d"), end=" ")
        num *= 2
    
    num //= 2
    for j in range(i):
        num //= 2
        print(format(num, "3d"), end=" ")
    
    print()
"""
num = 1
for i in range(8):
    for j in range(8 - i):
        print("    ", end="")
    
    for j in range(i + 1):
        print(format(num, "3d"), end=" ")
        num *= 2
    
    num //= 2
    for j in range(i):
        num //= 2
        print(format(num, "3d"), end=" ")
    
    for j in range(7 - i):
        print("   ", end="")
    
    print()
    
---------------------------
---------------------------------------------------

tuition = 10000  # Initial tuition
annual_increase = 0.05  # 5% increase each year

for year in range(1, 11):
    tuition *= (1 + annual_increase)  # Calculate tuition for each year
    if year == 1:
        print(f"Tuition in year {year}: ${tuition:.2f}")
    if year == 10:
        tuition_10th_year = tuition
        print(f"Tuition in year {year}: ${tuition:.2f}")

total_cost = 0

for year in range(11, 15):
    total_cost += tuition_10th_year
    tuition_10th_year *= (1 + annual_increase)

print(f"\nTotal cost of four years' worth of tuition after the tenth year: ${total_cost:.2f}")

-----------------------------------------
def divide_array(arr):
    total_sum = sum(arr)
    current_sum = 0
    left_part = []
    
    # Iterate through the array and add elements to the left_part
    # until the sum of left_part is half of the total_sum
    for num in arr:
        current_sum += num
        left_part.append(num)
        
        if current_sum == total_sum / 2:
            return left_part, arr[len(left_part):]
    
    return "Equal sum partition not possible"

# Example usage
arr = [6,7,2]
result = divide_array(arr)
print("The array is", result[0], "and", result[1])

------------------------------------
def divide_array(arr):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False

    target_sum = total_sum // 2
    current_sum = 0

    for num in arr:
        current_sum += num
        if current_sum == target_sum:
            return True
        elif current_sum > target_sum:
            return False

    return False

# Example usage
arr = [2,6,1,9]
result = divide_array(arr)
print(result)
-------------------------------------
"""
"""
tuition = 10000 
B= int( tuition*5/100)  


for year in range(1, 11):
    tuition += B
print("Tuition in 10 years:", tuition)
cost = 0
for year in range(11, 15):
    tuition += B
    cost += tuition
    


print("Total cost of 4 years, after the 10 year:", cost)
"""

