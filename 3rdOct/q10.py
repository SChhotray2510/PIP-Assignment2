def sum_of_even_digits(number):
    # Convert the number to a string
    num_str = str(number)
    
    # Use list comprehension to filter even digits and convert them back to integers
    even_digits = [int(digit) for digit in num_str if int(digit) % 2 == 0]
    
    # Calculate the sum of even digits using the sum() function
    return sum(even_digits)



num = int(input("Enter a four-digit number: "))
    
if 1000 <= num <= 9999:
 result = sum_of_even_digits(num)
 print(f"The sum of even digits in {num} is: {result}")
else:
 print("Please enter a valid four-digit number.")
