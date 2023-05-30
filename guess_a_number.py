import random

pc_number = random.randint(1, 100)

while True:
    player_turn = input("Познай числото от 1 до 100: ")

    if not player_turn.isdigit():
        print("Не позна!!!, Опитай пак...")
        continue
    player_number = int(player_turn)

    if player_number == pc_number:
        print("Ти позна, Браво")
        break
    elif player_number > pc_number:
        print("Твърде голямо число, опитай с по малко!")
    else:
        print("Твърде ниско число, опитай с по голямо!")





