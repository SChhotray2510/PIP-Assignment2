def UpperCase(char):
    if char.isalpha() and char.islower():
        return char.upper()
    else:
        raise ValueError("Input is not a valid lowercase alphabet.")

def main():
    
 user_input = input("Enter a lowercase alphabet: ")
        
 if len(user_input) == 1:
  result = UpperCase(user_input)
  print(f"The uppercase equivalent is: {result}")
 else:
  print("Please enter a single lowercase alphabet.")
    
main()
