import random

choices = ["камень", "ножницы", "бумага"]

user = input("Выбери: камень, ножницы или бумага: ").lower()
computer = random.choice(choices)

print("Компьютер выбрал:", computer)

if user not in choices:
    print("Ошибка: нужно написать камень, ножницы или бумага")
elif user == computer:
    print("Ничья!")
elif user == "камень" and computer == "ножницы":
    print("Ты победил!")
elif user == "ножницы" and computer == "бумага":
    print("Ты победил!")
elif user == "бумага" and computer == "камень":
    print("Ты победил!")
else:
    print("Компьютер победил!")
