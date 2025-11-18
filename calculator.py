import os

A = 0
B = 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    clear_screen()
    print("=== ПРОСТОЙ КАЛЬКУЛЯТОР ===")
    print(f"A = {A}, B = {B}")
    print("1. Ввести A")
    print("2. Ввести B") 
    print("3. Сложение (+)")
    print("4. Вычитание (-)")
    print("5. Умножение (*)")
    print("6. Деление (/)")
    print("0. Выход")
    print("========================")

def enter_A():
    global A
    try:
        A = float(input("Введите A: "))
        print(f"A = {A}")
    except:
        print("Ошибка! Введите число.")
    input("Нажмите Enter...")

def enter_B():
    global B
    try:
        B = float(input("Введите B: "))
        print(f"B = {B}")
    except:
        print("Ошибка! Введите число.")
    input("Нажмите Enter...")

def addition():
    """Сложение - РАБОЧЕЕ"""
    result = A + B
    print(f"{A} + {B} = {result}")
    input("Нажмите Enter...")

def subtraction():
    """Вычитание - НЕ РЕАЛИЗОВАНО"""
    print("Вычитание не реализовано")
    input("Нажмите Enter...")

def multiplication():
    """Умножение - НЕ РЕАЛИЗОВАНО"""
    print("Умножение не реализовано")
    input("Нажмите Enter...")

def division():
    """Деление - НЕ РЕАЛИЗОВАНО"""
    print("Деление не реализовано")
    input("Нажмите Enter...")

# Главная программа
while True:
    display_menu()
    choice = input("Выберите: ")
    
    if choice == "1":
        enter_A()
    elif choice == "2":
        enter_B()
    elif choice == "3":
        addition()
    elif choice == "4":
        subtraction()
    elif choice == "5":
        multiplication()
    elif choice == "6":
        division()
    elif choice == "0":
        print("Выход...")
        break
    else:
        print("Неверный выбор!")
        input("Нажмите Enter...")