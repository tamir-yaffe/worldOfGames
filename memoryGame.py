# game 2
# memory game 
# generate random numbers 
# show them for 1 sec 
# hide them 
# prompt for correct sequance

import random
import time
from iGame import GameInterface

class MemoryGame(GameInterface):
 
    difficulty = 0
   
    def __init__(self):
        pass
    
    def play(self,difficulty:int):
        self.difficulty = difficulty
        sequeance = self.__generate_number()
        input = self.__input_sequance()
        self.result = self.__result(sequeance,input)
        print(self.result)
        
        
    def __generate_number(self):
        sequence_list = []
        for i in range (self.difficulty):
            random_num = random.randrange(1,101)
            sequence_list.append(random_num)
        print(sequence_list,end='\r')
        time.sleep(1)
        print('hidden now your turn')
        return sequence_list
    
    def __result(self,guess_memory,sequence_list):
        return guess_memory == sequence_list
        
    def __input_sequance(self):
        guess_memory = []
        for i in range(self.difficulty):
            guess_item = int(input("enter the right sequance :"))
            guess_memory.append(guess_item)
        return guess_memory
