from game_stats import Game_stats

class Player(Game_stats):
    def __init__(self, name:str, surname:str, shirt_number:int, time_played:float, golas:int, assists:int, yellows:int, reds:int):
        super().__init__(time_played, golas, assists, yellows, reds)


        self._name = name
        self._surname = surname
        self._shirt_number = shirt_number


    def __repr__(self):
        return f'Name: {self.name}\nSurname: {self.surname}\nShirt number: {self.shirt_number}\n' \
               f'Time played: {self.time_played}\nGoals: {self.goals}\nAssists: {self.assists}\n' \
               f'Yellows: {self.yellows}\nRed: {self.reds}'

    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, name):
        self._name = name


    @property
    def surname(self):
        return self._surname


    @surname.setter
    def surname(self, surname):
        self._surname = surname


    @property
    def shirt_number(self):
        return self._shirt_number

    @shirt_number.setter
    def shirt_number(self, shirt_number):
        self._shirt_number = shirt_number
