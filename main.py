from guessGame import GuessGame
from memoryGame import MemoryGame
from userSettings import UserSettings
from currencyRouletteGame import CurrencyGame

class Main:
    
    def __init__(self):
        settings = UserSettings()
        setting = settings.load_game()
        #print(setting)
        self.start_game(setting['game'],setting['difficulty'])
        
    def start_game(self,selected_game:int,difficulty:int):
        if selected_game == 1 :
            game = MemoryGame()
        elif selected_game == 2 :
            game = GuessGame() 
        elif selected_game == 3 : 
            game = CurrencyGame()
        game.play(difficulty)
        
Main()

#prompt for user inputs
# - set name
# - select game
# - select dificulty

# game one
# prompt for guess
# output success or failer

# game 2
# memory game 
# generate random numbers 
# show them for 1 sec 
# hide them 
# prompt for correct sequance 

# game 3 
# currency game 
# make a converter for usd to ils 
# prompt for a guess of 