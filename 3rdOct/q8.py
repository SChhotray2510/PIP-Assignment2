def print_multiplication_table(number, n=10):

    print(f"Multiplication table for {number}:")
    for i in range(1, n + 1):
        result = number * i
        print(f"{number} x {i} = {result}")



number = int(input("Enter a number: "))
print_multiplication_table(number)

