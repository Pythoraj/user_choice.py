from IPython.display import clear_output
clear_output()
Game_List= [0,1,2]
def display_game (Game_list):
    print("Here is an actuale game list")
    print(Game_list)

def user_choice():
    choice = 'Wrong'
    while choice not in ['0', '1', '2']:

        choice = input("please enter a position to replace ['0','1','2']")
        if choice not in ['0', '1', '2']:
            clear_output()
            print("Sorry,but you did not chopse correct position [0,1,2]")
    return int(choice)
def replacement_choice(Game_List, position):
    User_replacement= input("please enter your string for replace")
    Game_List[position]=User_replacement
    return Game_List

def gameon_choice():
    choice = "wrong"
    while choice not in ['Y', 'N']:
        choice = input("Would you like to keep playing game? Y or N : ")

        if choice not in ['Y', 'N']:
            print("Sorry, I did not understand. Please make sure choose Y or N to continue playing the game: ")
            clear_output()
    if choice in 'Y':
        return True
    else:
        return False

Game_On=True
Game_List=[0,1,2]
while Game_On:
    clear_output()
    display_game(Game_List)
    position= user_choice()
    Game_List= replacement_choice(Game_List, position)
    clear_output()
    display_game(Game_List)
    Game_On = gameon_choice()