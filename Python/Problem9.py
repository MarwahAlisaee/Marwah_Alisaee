def calculate(num):
    sum1 = sum(num[0])
    sum2 = sum(num[2])
    sum3 = num[0][0] + num[1][1] + num[2][2]
    sum4 = num[0][2] + num[1][1] + num[2][0]

    

    print(f"{num[0][0]} + {num[1][1]} + {num[2][2]} = {sum3}")
    print(f"{num[0][2]} + {num[1][1]} + {num[2][0]} = {sum4}")
    print(f"|{sum3} - {sum4}| = {abs(sum3 - sum4)}")


input_nember = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]

calculate(input_nember)
