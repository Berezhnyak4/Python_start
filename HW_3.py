"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
 Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# def delenie(x,y):
#
#     if y == 0:
#         print("Деление на ноль")
#     else:
#         return x/y
# print(delenie(x,y))

"""2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя,
 фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как 
 именованные аргументы. Реализовать вывод данных о пользователе одной строкой."""
# dict_1 = {"имя":None, "фамилия":None, "год рождения":None, "город проживания":None, "email":None, "телефон":None}
# name = input("Enter name: ")
# sern = input("Enter sername: ")
# gr = input("Enter age: ")
# gp = input("Enter youe city: ")
# email = input(" Enter email: ")
# tel = input("Enter telephon number: ")
# def data(name,sern,gr,gp,email,tel):
#     dict_1["имя"] = name
#     dict_1["фамилия"] = sern
#     dict_1["год рождения"] = gr
#     dict_1["город проживания"]= gp
#     dict_1["email"] = email
#     dict_1["телефон"] = tel
#     return dict_1
# print (data(name,sern,gr,gp,email,tel))
"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
 наибольших двух аргументов."""
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
# def my_func(a,b,c):
#     sum = a + b + c - min(a,b,c)
#     return sum
# print(f'Сумма наибольших аргументов {my_func(a,b,c)}')
"""4. Программа принимает действительное положительное число x и целое отрицательное число y. 
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции 
my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в
 степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью
 оператора **. Второй — более сложная реализация без оператора **, предусматривающая использование 
 цикла."""
x = int(input(" Enter x: "))
y = int(input("Enter -y: "))

def my_func(x,y):
    step = x**y
    return step
print(my_func(x,y))

def my_func_2(x,y):
    res = 1
    for i in range(abs(y)):
        res*=x
    return 1/res
print(my_func_2(x,y))

"""5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter
 должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и 
 снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
  вместо числа вводится специальный символ, выполнение программы завершается. Если специальный 
  символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной 
  ранее сумме и после этого завершить программу."""

"""6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую 
его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
 Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое
  слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию 
  int_func()."""