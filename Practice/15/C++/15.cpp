﻿// 15.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <cstdlib>
using namespace std;
int main()
{
    setlocale(0, "");
    int vixod, vibor, max;
    int a, b, x, i, n, s; //a, b -диапазон рандома, x - чило рандома, n - догадка s - количество попыток
    
    do
    {
        
        cout << "установить свои значения? 1-да ";
        cin >> vibor;
        if (vibor == 1){
            cout << "введите диапазон\n";
            cin >> a >> b;
            if (a > b) { max = b; b = a; a = max; }
            cout << "введите количество попыток\n";// данные действия для удобства изменения основных параметров игры, не меняя код.
            cin >> s; }
        else { a = 0; b = 100; s = 5; }
        x = rand() % (b - a + 1) + a; // если сделать диапазон рандома и количество попыток постоянными, то просто убрать ввод этих переменных, и заменить их на постоянные значения.
        i = 0;
        cout << "Добро пожаловать в игру, у вас есть "<< s<<" попыток чтобы отгадать число от "<<a<<" до "<<b;
        while (i < s)
        {
            cout << "\n Введите догадку\n";
            cin >> n;
            if (n == x && n >= a && n <= b)
            {cout << "----------Поздравляю, вы выиграли----------"; i = s;}
            else if (n != x && n >= a && n <= b)
            {
                i++;
                if (i < s)
                {
                    if (n > x) { cout << "\nНеудача, осталось " << s - i << " попытки, загаданное число меньше чем " << n; }
                    else { cout << "\nНеудача, осталось " << s - i << " попытки, загаданное число большее чем " << n; }
                }
                else { cout << "\n     -----Вы проиграли, было загаданно: " << x << "-----     "; }
            }
            else { cout << "\n     !!!   число не в заданном диапазоне   !!!     "; }
        }
        cout << "\nначать заново? 1-да\n";
        cin >> vixod;
    } while (vixod == 1);
} 


