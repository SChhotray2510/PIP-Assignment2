def evaluate_expression(expression):
    
 result = eval(expression)
 return result
    

user_expression = input("Enter an arithmetic expression: ")
result = evaluate_expression(user_expression)
print(f"Result of the expression '{user_expression}' is: {result}")
