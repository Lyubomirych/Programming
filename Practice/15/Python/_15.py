import random
#!/usr/bin/env python3

def main():
    vibor = input("хотите ввести свои значения? y-да ")
    if vibor == "y":
        a, b = input("Введите диапазон чисел: ").split()
        a = int(a) 
        b = int(b)
        if a > b: 
            a , b = b , a
        p = input("Введите количество попыток: ")
        p = int(p)
    else: 
        a, b, p = 0, 100, 5 
    print("--------------------Добро пожаловать в игру, у вас есть ", p, " попыток чтобы отгадать число от ", a, " до ", b,"----------------")
    x = random.randint(a, b)
    i = 0
    while i<p:
        n = int(input("Введите догадку: "))
        if n==x and n>=a and n<=b:
            print("-------------------------------------------Поздравляюм, вы угадали-------------------------------------------")
            i=p
        elif n!=x and n>=a and n<=b:
            i = i + 1
            if i<p:
                if n>x:
                    print("--неудача, осталось", p-i, " попыток, загаданное число меньше чем ", n)
                else:
                    print("--неудача, осталось", p-i, " попыток, загаданное число больше чем ", n)
            else: 
                print("--------------------------------------Вы проиграли, загаданное число:", x, "-------------------------------------------")
        else: 
            print("                               !!!!!!!     число не в загаданном диапазоне     !!!!!!!")
    esc = int(input("Начать сначала? 1-да: "))
    if esc!=1:
       quit(0)
if __name__ == '__main__':
    while True:  
        main()






