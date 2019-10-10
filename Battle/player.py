import csv
from Battle.constants_battle import LIST_FIGHTERS_FILE


class Player():

    def __init__(self, number_player):
        with open(LIST_FIGHTERS_FILE, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for line in csv_reader:
                if line['data'] == number_player:
                    self.name = line['name']
                    self.power = int(line['power'])
                    self.skill = int(line['skill'])
                    self.health = int(line['health'])
                    break

    def get_health(self):
        return self.health

    def get_power(self):
        return self.power

    def get_skill(self):
        return self.skill

    def set_health(self, new_health):
        self.health = new_health

    # def show_player(self):
    #     print("{} - HP = {}".format(self.name, self.health))

    @property
    def damag(self):
        return self.get_power() * self.get_skill()

    @property
    def warrior_parameters(self):
        return self.power, self.skill, self.health

    def __eq__(self, other):
        print('\nСравним Воинов на полное равенство их параметров:')
        if self.warrior_parameters == other.warrior_parameters:
            return print(" Воины по всем паметрам равны!!! ")
        return print("Воины по параметрам НЕ равны")

    def __gt__(self, other):
        if self.health > other.health:
            difference = self.health - other.health
            return print('У воина', self.name, 'HP больше на', difference, 'едениц чем у воина', other.name)
        else:
            difference = other.health - self.health
            return print('У воина', self.name, 'HP меньше на', difference, 'едениц чем у воина', other.name)

    def __str__(self):
        return "{} - HP = {}".format(self.name, self.health)
