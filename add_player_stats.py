from player import Player

#name:str, surname:str, shirt_number:int, time_played, golas:int, assists:int, yellows:int, reds:int
def add_player():
    name = input("Player name: ")
    surname = input("Player surname: ")
    shirt_number = int(input("Shirt number: "))
    time_played = float(input("Time played: "))
    goals = int(input("Goals scored: "))
    assists = int(input("Assists: "))
    yellows = int(input("Yellows cards: "))
    reds = int(input("Red card: "))


    player = Player(name, surname, shirt_number, time_played, goals, assists, yellows, reds)
    return player
