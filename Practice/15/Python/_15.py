import random
#!/usr/bin/env python3

def main():
    print("--------------------Добро пожаловать в игру, у вас есть 5 попыток чтобы отгадать число от 0 до 100--------------------")
    x = random.randint(0, 100)
    i = 0
    while i<5:
        n = int(input("Введите догадку: "))
        if n==x and n>=0 and n<=100:
            print("-------------------------------------------Поздравляюм, вы угадали-------------------------------------------")
            i=5
        elif n!=x and n>=0 and n<=100:
            i = i + 1
            if i<5:
                if n>x:
                    print("--неудача, осталось", 5-i, " попыток, загаданное число меньше чем ", n)
                else:
                    print("--неудача, осталось", 5-i, " попыток, загаданное число больше чем ", n)
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






