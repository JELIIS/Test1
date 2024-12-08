import random
import f
def game():
    rounds = int(input("Сколько раз вы хотите играть: "))
    for i in range(rounds):
        name, date = random.choice(list(f.famous_people.items()))
        answer = input(f"Когда родился {name}: ")
        if answer == date:
            print("Верно")
            f.famous_people.pop(name)
        else:
            print("Неверно")
    print("Пока")