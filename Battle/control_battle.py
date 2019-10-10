import random
from Battle.player import Player
from Battle.constants_battle import *


class ControlBattle():


    def user_choice_action(self, value):
        """ Метод проверяет правильность выбора Игроком предлагаемых вариантов действий (1,2,3)"""
        while True:
            try:
                template = TEMPLATE
                data = int(input('{}'.format(value)))
                if data in template:
                    return data
                print(PLEASE_RETYPE_MESSAGE)
            except ValueError:
                print(PLEASE_RETYPE_MESSAGE)

    def get_random_data(self):
        """Метод случайного выбора оппонента и его действий"""
        return random.randint(1, 3)

    def select_kick_block(self):
        """Метод выбора параметров удара и блока"""
        kick = self.user_choice_action(SELECT_KICK_MESSAGE)
        block = self.user_choice_action(SELECT_BLOCK_MESSAGE)
        return kick, block

    def check_end_game(self, warrior, opponent):
        """Метод контроля окончания БОЯ"""
        if warrior.get_health() <= 0:
            return True, False
        if opponent.get_health() <= 0:
            return True, True
        return False, None

    def control_battle(self):
        """Метод контроля БОЯ"""
        print(START_GAME_MESSAGE)

        number_player = input(SELECT_WARRIOR_MESSAGE)
        warrior = Player(number_player)

        opponent_random = str(self.get_random_data())
        opponent = Player(opponent_random)

        warrior == opponent  # Сравним Воинов на полное равенство их параметров:
        warrior > opponent  # Сравнение у какого воина больше НР

        warrior_win = True

        while True:  # Основной цикл ИГРЫ
            print('Opponent: ', opponent)
            print('Your warrior: ', warrior)
            print()  # для визуального разделения хода игры

            kick, block = self.select_kick_block()

            print()  # для визуального разделения хода игры

            opponent_kick = self.get_random_data()
            opponent_block = self.get_random_data()

            if kick != opponent_block:
                print('You hit an opponent!')
                opponent.set_health(opponent.get_health() - warrior.damag)

            if block != opponent_kick:
                print('Opponent hit you :( ')
                warrior.set_health(warrior.get_health() - opponent.damag)

            exit_circle, warrior_win = self.check_end_game(warrior, opponent)
            if exit_circle:
                break

        if warrior_win:
            print(WINNER_MESSAGE)
        else:
            print(GAME_OVER)
