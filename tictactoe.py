ef display():
  return("__|__|__ \n__|__|__ \n  |  |\n 1. 2. 3. \n 4. 5. 6. \n 7. 8. 9.")

# selecting X and O 
# each inputs
def inputs():
  inputside = input("Enter which side you want to be (Xs or Os): ")
  input1 = input("Enter the number to choose: ")
  if input1 == "1" and inputside == "X":
    return ("X _ _")
  elif input1 == "1" and inputside == "X":
    return ("X _ _")

def inputs2():
  inputside = input("Enter which side you want to be (Xs or Os): ")
  input2 = input("Enter the number to choose: ")
  if input2 == "2" and inputside == "O":
    return ("X O _")

def inputs2():
  inputside = input("Enter which side you want to be (Xs or Os): ")
  input2 = input("Enter the number to choose: ")
  if input2 == "2" and inputside == "O":
    return ("X O _")

print(display())
print(inputs())
print(inputs2())
