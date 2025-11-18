class Calculator:
    def __init__(self):
        self.a = None
        self.b = None
    
    def display_menu(self):
        print("\n=== Калькулятор ===")
        print("1. Ввести A")
        print("2. Ввести B") 
        print("3. Выполнить операцию '+'")
        print("4. Выполнить операцию '-'")
        print("5. Выполнить операцию '*'")
        print("6. Выполнить операцию '/'")
        print("0. Выход")
    
    def input_a(self):
        try:
            self.a = float(input("Введите число A: "))
            print(f"Число A установлено: {self.a}")
        except ValueError:
            print("Ошибка: введите корректное число")
    
    def input_b(self):
        try:
            self.b = float(input("Введите число B: "))
            print(f"Число B установлено: {self.b}")
        except ValueError:
            print("Ошибка: введите корректное число")
    
    def add(self):
        if self.a is not None and self.b is not None:
            result = self.a + self.b
            print(f"Результат: {self.a} + {self.b} = {result}")
        else:
            print("Ошибка: сначала введите числа A и B")
    
    def subtract(self):
        if self.a is not None and self.b is not None:
            result = self.a - self.b
            print(f"Результат: {self.a} - {self.b} = {result}")
        else:
            print("Ошибка: сначала введите числа A и B")
    
    def multiply(self):
        if self.a is not None and self.b is not None:
            result = self.a * self.b
            print(f"Результат: {self.a} * {self.b} = {result}")
        else:
            print("Ошибка: сначала введите числа A и B")
    
    def divide(self):
        if self.a is not None and self.b is not None:
            if self.b != 0:
                result = self.a / self.b
                print(f"Результат: {self.a} / {self.b} = {result}")
            else:
                print("Ошибка: деление на ноль")
        else:
            print("Ошибка: сначала введите числа A и B")

def main():
    calc = Calculator()
    
    while True:
        calc.display_menu()
        choice = input("Выберите пункт меню: ")
        
        if choice == '1':
            calc.input_a()
        elif choice == '2':
            calc.input_b()
        elif choice == '3':
            calc.add()
        elif choice == '4':
            calc.subtract()
        elif choice == '5':
            calc.multiply()
        elif choice == '6':
            calc.divide()
        elif choice == '0':
            print("Выход из программы")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()