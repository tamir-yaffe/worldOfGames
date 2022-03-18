# game one
# generate random number 
# prompt for guess
# compare to diffculty
# output success or failer

import random
from iGame import GameInterface

class GuessGame(GameInterface):
    
    def __init__(self):
        pass
    
    def play(self,difficulty):
         self.secret_number = self.__generate_number(difficulty)
         self.guess = self.__get_guess_from_user()
         self.result = self.__compare_results(self.guess,self.secret_number)
         print(self.result)
    
    def __generate_number(self,difficulty):
       return random.randrange(0 , difficulty)
        
    def __get_guess_from_user(self):
        self.guess = input("Enter number :")
        if self.guess.isdecimal() == False:
            self.__get_guess_from_user()
        return self.guess
    
    def __compare_results(self,guess,secret_number):
        return secret_number == guess