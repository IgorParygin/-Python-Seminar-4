# a) Добавьте игру против бота

from random import randint

def check_number(name):
    x = int(input(f"{name}, введите, сколько конфет вы возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def view(name, k, candy):
    print(f"{name} сходил, он взял {k}, Осталось на столе {candy} конфет.")

player1 = input("Введите имя игрока: ")
player2 = "bot"
candy = 150
priority = randint(0, 1)
if priority:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

count1 = 0
count2 = 0

while candy > 28:
    if priority:
        k = check_number(player1)
        count1 += k
        candy -= k
        priority = False
        view(player1, k, candy)
    else:
        k = randint(1,29)
        count2 += k
        candy -= k
        priority = True
        view(player2, k, candy)

if priority:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")
