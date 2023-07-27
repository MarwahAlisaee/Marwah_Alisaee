
def print_pattern():
    rows = 5
    cols = 12

    for i in range(rows):
        for j in range(cols):
            if i + j >= rows - 1 and j - i <= rows - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

    for i in range(rows - 1, -1, -1):
        for j in range(cols):
            if i + j >= rows - 1 and j - i <= rows - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


print_pattern()

