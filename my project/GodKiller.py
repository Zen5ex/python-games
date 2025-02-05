from colorama import *
from colorama import Fore, Style, init
import time
import sys
import os
import requests





# Инициализация colorama
init(autoreset=True)

# Объемный текст "Godkiller"
text_art = [
    "_______   ______    _______   __  ___  __   __       __       _______ .______",
    "/  _____| /  __  \  |       \ |  |/  / |  | |  |     |  |     |   ____||   _  \  ",
    "|  |  __  |  |  |  | |  .--.  ||  '  /  |  | |  |     |  |     |  |__   |  |_)| ",
    "| |_ | |  |  |  | |  |  |  ||    <   |  | |  |  |  |  |   __|  |      / |     |",
    "|  |__| | |  `--'  | |  '--'  ||  .  \  |  | |  `----.|  `----.|  |____ |  |\  \----.  ",
    "\______|  \______/  |_______/ |__|\__\ |__| |_______||_______||_______|| _| `._____|",
                                                
]    


# Определяем цвета для каждой строки
colors = [Fore.RED]

# Выводим объемный текст с цветами
for i, line in enumerate(text_art):
    print(colors[i % len(colors)] + line)
    time.sleep(0.2)  # Задержка для эффекта анимации

# Сброс цвета в конце
print(Style.RESET_ALL)

def bomb():
    print("🔴 Boom! Это была бомба!")

def dash():
    print("🏃💨 Вперед! Быстрый бег!")

def evil():
    print("😈 Мwahaha! Я злодей!")

def main():
    while True:
        print("\nМеню:")
        print("1: Bomb")
        print("2: Dash")
        print("3: Evil")
        print("4: Выход")

        choice = input("Введите номер опции: ")

        if choice == "1":
            bomb()
        elif choice == "2":
            dash()
        elif choice == "3":
            evil()
        elif choice == "4":
            print("Выход из программы...")
            break
        else:
            print("Некорректный выбор, пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()