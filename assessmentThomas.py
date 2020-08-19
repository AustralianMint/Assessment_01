#bejeweled Game assessment.

jewels = [[1, 2, 3],[4, 4, 5],[5, 3, 4]]

#print game board
def gameBoard():
    print(jewels[0])
    print(jewels[1])
    print(jewels[2])


#swap jewels fucntion
def swapJewels(jewels, row1, number1, row2, number2):
    jewels[row1][number1], jewels[row2][number2] = jewels[row2][number2], jewels[row1][number1]


gameBoard()

#Select row and number to switch.
row1 = int(input("Which row do you choose: "))
number1 = int(input("What number do you choose: "))

row2 = int(input("Which row do you choose: "))
number2 = int(input("What number do you choose: "))

#Make swap and print board
swapJewels(jewels, row1, number1, row2, number2)
gameBoard()


#Check if row is complete
if(len(set(jewels[0]))==1):
    print("THIS IS A VALID MOVE \n")
else:
    print("NUMBERS DO NOT MATCH \n")

if(len(set(jewels[1]))==1):
    print("THIS IS A VALID MOVE \n")
else:
    print("NUMBERS DO NOT MATCH \n")

if(len(set(jewels[2]))==1):
    print("THIS IS A VALID MOVE \n")
else:
    print("NUMBERS DO NOT MATCH \n")





