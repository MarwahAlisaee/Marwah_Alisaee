"""
def check_storage_capacity(storage_capacity, num_files, file_size):
    total_size = num_files * file_size
    if total_size <= storage_capacity:
        return "Yes"
    else:
        return "No"

# Taking input from the user
input_values = input("Enter storage capacity, number of files, and size of each file (space-separated): ")
x, n, y = map(int, input_values.split())

# Checking storage capacity
result = check_storage_capacity(x, n, y)
print(result)
"""

# Read input from file
with open("file_4.txt", "r") as file:
    storage_capacity, num_files, file_sizes = map(int, file.readline().strip().split())
    sizes = list(map(int, file.readline().strip().split()))

# Check storage capacity
results = []
for size in sizes:
    if num_files * size <= storage_capacity:
        results.append("Yes")
    else:
        results.append("No")

# Write output to file
with open("file_4.txt", "w") as file:
    file.write('\n'.join(results))
