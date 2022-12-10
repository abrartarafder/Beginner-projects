def displ():
  return ("TICTACTOE GRID \n_ _ _ \n_ _ _\n_ _ _ \n")
def inputs():
  displayx__ = "X _ _"
  displayxx_ = "X X _"
  displayxxx = "X X X"
  displayx_x = "X _ X"
  displayxo_ = "X O _"
  displayxoo = "X O O"
  displayxox = "X O X"
  displayxxo = "X X O"
  display_x_ = "_ X _"
  display_xx = "_ X X"
  display_xo = "_ X O"
  display__x = "_ _ X"
  displayo__ = "O _ _"
  displayoo_ = "O O _"
  displayooo = "O O O"
  displayo_o = "O _ O"
  displayox_=  "O X _"
  displayo_x=  "O _ X"
  displayoxx=  "O X X"
  displayoxo=  "O X O"
  displayoox=  "O O X"
  display_o_ = "_ O _"
  display_oo = "_ O O"
  display_ox = "_ O X"
  display__o = "_ _ O"
  display___ = "_ _ _"

  
  inputside1 = input("Enter which side you want to be (Xs or Os): ")
  # 1 and X
  input1 = input("Enter the number to choose: ")
  if input1 == "1" and inputside1 == "X":
    print(displayx__)
  if input1 == "2" and inputside1 == "X":
    print(display_x_)
  if input1 == "3" and inputside1 == "X":
    print(display__x)
  if input1 == "4" and inputside1 == "X":
    print(f'{display___} \n{displayx__}')
  if input1 == "5" and inputside1 == "X":
    print(f'{display___} \n{display_x_}')
  if input1 == "6" and inputside1 == "X":
    print(f'{display___} \n{display__x}')
  if input1 == "7" and inputside1 == "X":
    print(f'{display___} \n{display___} \n{displayx__}')
  if input1 == "8" and inputside1 == "X":
    print(f'{display___} \n{display___} \n{display_x_}')
  if input1 == "9" and inputside1 == "X":
    print(f'{display___} \n{display___} \n{display__x}')

  if input1 == "1" and inputside1 == "O":
    print(displayo__)
  if input1 == "2" and inputside1 == "O":
    print(display_o_)
  if input1 == "3" and inputside1 == "O":
    print(display__o)
  if input1 == "4" and inputside1 == "O":
    print(f'{display___} \n{displayo__}')
  if input1 == "5" and inputside1 == "O":
    print(f'{display___} \n{display_o_}')
  if input1 == "6" and inputside1 == "O":
    print(f'{display___} \n{display__o}')
  if input1 == "7" and inputside1 == "O":
    print(f'{display___} \n{display___} \n{displayo__}')
  if input1 == "8" and inputside1 == "O":
    print(f'{display___} \n{display___} \n{display_o_}')
  if input1 == "9" and inputside1 == "O":
    print(f'{display___} \n{display___} \n{display__o}')
  


    
  inputside2 = input("Enter which side you want to be (Xs or Os): ")
  input2 = input("Enter the number to choose: ")
  if input1 == "1" and inputside1 == "X" and input2 == "2" and inputside2 == "O":
    print(displayxo_)
  if input1 == "1" and input2 == "2" and inputside1 == "O" and inputside2 == "O":
    print(displayoo_)
  if input1 == "1" and input2 == "2" and inputside1 == "X" and inputside2 == "X":
    print(displayxx_) 
  if input1 == "1" and input2 == "3" and inputside1 == "X" and inputside2 == "X":
    print(displayx_x)
  if input1 == "3" and input2 == "1" and inputside1 == "X" and inputside2 == "X":
    print(displayx_x)
  if input1 == "3" and inputside1 == "X" and input2 == "2" and inputside2 == "X":
    print(display_xx)
  if input1 == "4" and inputside1 == "X" and input2 == "1" and inputside2 == "X":
    print(f'{displayx__} \n{displayx__}')

  
  inputside3 = input("Enter which side you want to be (Xs or Os): ")
  input3 = input("Enter the number to choose: ")
  if input1 == "1" and input2 == "2" and input3 == "3" and inputside1 == "X" and inputside2 == "X" and inputside3 == "X":
    print(displayxxx)
  if input1 == "1" and input2 == "3" and input3 == "2" and inputside1 == "X" and inputside2 == "X" and inputside3 == "X":
    print(displayxxx)
  if input1 == "3" and inputside1 == "X" and input2 == "2" and inputside2 == "X" and inputside3 == "X" and input3 == "1":
    print(displayxxx)
  if input1 == "1" and inputside1 == "X" and input2 == "2" and inputside2 == "O" and inputside3 == "O" and input3 == "3":
    print(displayxoo)
  if input1 == "1" and inputside1 == "X" and input2 == "2" and inputside2 == "O" and inputside3 == "X" and input3 == "3":
    print(displayxox)
  if input1 == "3" and inputside1 == "X" and input2 == "1" and inputside2 == "X" and inputside3 == "X" and input3 == "2":
    print(displayxxx)
  if input1 == "1" and inputside1 == "X" and input2 == "2" and inputside2 == "X" and inputside3 == "O" and input3 == "3":
    print(displayxxo)
  if input1 == "7" and inputside1 == "X" and input2 == "4" and inputside2 == "X" and inputside3 == "X" and input3 == "1":
    print(f'{displayx__} \n{displayx__} \n{displayx__}')
  if input1 == "4" and inputside1 == "X" and input2 == "1" and inputside2 == "X" and input3 == "7" and inputside3   == "X":
    print(f'{displayx__} \n{displayx__}\n{displayx__}')
  
  
  
  
  
  
  
  
  
  return ""
print(displ())
print(inputs())
