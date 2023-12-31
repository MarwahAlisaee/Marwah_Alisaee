def count_improvements(progress):
    count = 0
    max_distance = progress[0]

    for distance in progress:
        if distance > max_distance:
            count += 1
            max_distance = distance

    return count

# Prompt the user to enter Salim's progress
progress_input = input("Enter Salim's progress (comma-separated distances): ")
progress = [int(distance) for distance in progress_input.split(",")]

# Calculate the number of improvements
improvements = count_improvements(progress)
print("Number of improvements:", improvements)