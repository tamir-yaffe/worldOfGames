#prompt for user inputs
# - set name
# - select game
# - select dificulty

class UserSettings:
    
    setting = {}

    def __init__(self):
        pass

    def load_game(self):
        self.__get_name()
        self.__select_game()
        self.__set_difficulty()
        return self.setting
    
    def __get_name(self):
        self.setting['name'] = input("Enter your name:")
        print("Hello", self.setting['name'], 'and welcome to the World of Games(WoG).\n Here you can find many cool games to play \n')

    def __select_game(self):
        self.setting['game'] = input("Choose a game with the numbers 1-3:\n1 = Memory game \n2 = Guess Game \n3 = Currency game\n")
        if self.setting['game'].isdecimal() == False:
            self.load_game()
        else:
            self.setting['game'] = int(self.setting['game'])
            game_selection_map = {
                1 : "Memory game",
                2 : "Guess game",
                3 : "Currency game"
            }
            
            print("\n" + game_selection_map[self.setting['game']])
           

    def __set_difficulty(self):
        self.setting['difficulty'] = input("\nChoose the difficulty you want to play 1-5\n1-Easy as hell\n2-ahh\n3-okyy...\n4-WHAT?!\n5-What the ****\n")
        if self.setting['difficulty'].isdecimal() == False:
            self.load_game()
        else:
            self.setting['difficulty'] = int(self.setting['difficulty'])
            difficulty_selection_map = {
                1 : "Easy as hell",
                2 : "ahh",
                3 : "okyy...",
                4 : "WHAT?!",
                5 : "WTF?!"
            }
            print("\n" + difficulty_selection_map[self.setting['difficulty']])

        print("\nGood Luck & have fun LOL(evil laugh)")
