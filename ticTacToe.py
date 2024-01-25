#Player1 and Player2
#record who goes where using user_input from (1-9)
#P1 goes first
#P2 goes second
#P1 is X
#P2 is O
#Check after every turn if a 3 in a row of the same type of marker has been made
#If not keep playing
#If so stop and declare who won (by having three of the same marker in a row)
#If all 9 cells are filled and there is no winner, declare tie and ask to keep playing and reset board

grid = [0,1,2,3,4,5,6,7,8]
game_over = False
turn = 1
def print_grid():
    if len(grid) != 9:
        print("Error: The grid should contain exactly 9 items.")
        return

    for i in range(0, 8, 3):
        # grid[i] | grid[i + 1] | grid[i + 2]
        print(str(grid[i]) + " | " + str(grid[i + 1]) + " | " + str(grid[i + 2]))
        if i < 6:
            print("---------")
while turn < 10 and game_over == False:
    
    print_grid()
    user_input = input("What square do you want to place your item in? ")
    while not user_input.isnumeric() or int(user_input) < 0 or int(user_input) > 8:
        print("Not a valid answer")
        user_input = input("What square do you want to place your item in? ")

    print(user_input)

    if turn % 2 == 1:
        grid[int(user_input)] = "X"
    else:
        grid[int(user_input)] = "O"
            #X checking row
    
    if grid[0] == grid[1] and grid[1] == grid[2]:
        game_over = True
        if grid[0] == "X":
            print("Player 1 Wins")
        else:
             print("Player 2 Wins")

    if grid[3] == grid[4] and grid[4] == grid[5]:
        game_over = True
        if grid[3] == "X":
            print("Player 1 Wins")
        else:
             print("Player 2 Wins")

    if grid[6] == grid[7] and grid[7] == grid[8]:
        game_over = True
        if grid[6] == "X":
            print("Player 1 Wins")
        else:
             print("Player 2 Wins")

    if grid[0] == grid[3] and grid[3] == grid[6]:
        game_over = True
        if grid[0] == "X":
            print("Player 1 Wins")
        else:
             print("Player 2 Wins")

    if grid[1] == grid[4] and grid[4] == grid[7]:
        game_over = True
        if grid[1] == "X":
            print("Player 1 Wins")
        else:
             print("Player 2 Wins")

    if grid[2] == grid[5] and grid[5] == grid[8]:
        game_over = True
        if grid[2] == "X":
            print("Player 1 Wins")
        else:
             print("Player 2 Wins")  

    if grid[0] == grid[4] and grid[4] == grid[8]:
        game_over = True
        if grid[0] == "X":
            print("Player 1 Wins")
        else:
             print("Player 2 Wins")   

    if grid[2] == grid[4] and grid[4] == grid[6]:
        game_over = True
        if grid[2] == "X":
            print("Player 1 Wins")
        else:
             print("Player 2 Wins")      
    turn += 1
print_grid()


#WHAT NEEDS TO BE DEBUGGED
    #Why break wasn't working
    # Why Game over and diagnol line prints so many times





#Use while loop to make game run until 3 cells are set in a row column or diagnol line are equal to "X" or all 9 cells are filled
#flip turns using modulo (%) using even or oddd value exa. %2