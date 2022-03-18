# game 3
# currency game
# make a converter for usd to ils
# prompt for a guess of
# https://v6.exchangerate-api.com/v6/0f24c140d6ef4a352d66cb96/latest/USD api request
import random
import requests
from iGame import GameInterface

class CurrencyGame(GameInterface):
    
    def __init__(self):
        pass

    def play(self, difficulty:int):
        amount = self.__get_money_interval(difficulty)
        guess_rate = self.__get_guess_from_user()
        result = self.__compare_results(amount, guess_rate)
        print(result)

    def __get_money_interval(self, difficulty):
        random_amount = random.randint(0, 100)
        print(random_amount)
        precision = random_amount + (5 - difficulty)
        return self.__get_Convertion_rate() * precision
        # free currency api converter used as class member
        # difficulty , total money value  = random_amount , interval its the distance between random_amount to difficulty
        # the interval will be random_amount-(5-difficulty),random_amount+(5-difficulty)

    def __get_Convertion_rate(self):
        response_usd = requests.get(
            "https://v6.exchangerate-api.com/v6/0f24c140d6ef4a352d66cb96/pair/USD/ILS")
        # i can use the info inside this object
        return response_usd.json()['conversion_rate']

    def __get_guess_from_user(self):
        self.guess_rate = int(input("Enter the amount of USD in ILS:"))
        return self.guess_rate

    def __compare_results(self, amount, guess_rate):
        return amount == guess_rate