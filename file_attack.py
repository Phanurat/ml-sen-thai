filename = "who/attack_ps.txt"
with open(filename, 'r', encoding='utf-8') as file:
    who = file.readlines()

    print(who[1])
    for whos in who:
        pass