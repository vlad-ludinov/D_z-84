def print_multiplication_table(n: int):
    print()
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(F"{i} * {j} = {i*j}")
        print()


print_multiplication_table(10)
