print("This program will print out all of the odd numbers within the range inputted") # Explains what the program does

try: # Catches + handles exceptions
  x = int(input("Select the min value of the range: ")) #Prompts user to input the min value 
  y = int(input("Select the max value of the range: ")) #Prompts user to input the max value

  while x < y: # As long as the min value is less than the max value...
    if (x % 2) == 0: # Checks if the remainder of the min value is 0 after being divided by any even number
      x += 1 # If the remainder is relative to 0, move onto the next number
    else: # If the remainder is not relative to 0 it is odd
      print(x) # Prints odd number
      x += 1 # Moves onto the next number
except Exception as e: # Declares variable e as the exception 
  print(e) # Prints out the exception 