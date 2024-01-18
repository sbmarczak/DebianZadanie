#!/usr/bin/env python3

def kalkulator():
    while True:
        print("1. Dodawanie")
        print("2. Odejmowanie")
        print("3. Mnożenie")
        print("4. Dzielenie")
        print("5. Wyjście")
        wybor = input("Wybierz operację (1/2/3/4/5): ")

        if wybor == '5':
            print("Koniec programu.")
            break

        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))

        if wybor == '1':
            print("Wynik: ", num1 + num2)
        elif wybor == '2':
            print("Wynik: ", num1 - num2)
        elif wybor == '3':
            print("Wynik: ", num1 * num2)
        elif wybor == '4':
            if num2 != 0:
                print("Wynik: ", num1 / num2)
            else:
                print("Błąd! Nie można dzielić przez zero.")
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

kalkulator()
