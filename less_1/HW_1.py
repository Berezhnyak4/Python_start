"""1 Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран."""
# a = 1.4
# b = "afa"
# c = False
# d = int(input( "Input number: "))
# print(a,b,c,d)
# name = input(" What you name? ")
# age = int(input( "What you age: "))
# print(a, b, c)
# print( "Name: " + name + "; Age:", age)

"""2  Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк."""
# tm = int(input("Enter the number of seconds: "))
# hour = tm//3600
# minut = tm%3600//60
# sec = tm%60
#
# print(f"Время в формате чч:мм:сс   {hour:02}:{minut:02}:{sec:02}.")

"""3 Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369."""
# e = input("Input number: ")
# sum = int(e) + int(e+e) + int(e + e + e)
# print(sum)

"""4 Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции."""
# f = int(input("Input number: "))
#
# m = f%10
# f = f//10
# while f > 0:
#     if f%10 > m:
#         m = f%10
#     f = f//10
# print("The biger number ", m)

"""5  Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника."""
# pr = int(input("Input your profit: "))
# ct = int(input("Input your cost: "))
# if pr<ct:
#     print("You looser")
# elif pr>ct:
#     prof = (pr-ct)/pr*100
#     print(f"{prof} % profitability")
#     people = int(input("Input numbers your employees: "))
#     print(f"Profit for person: {(pr-ct)/people} euro")
# else:
#     print("Profit is equal cost")

"""6 Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня."""
# n = int(input("Input your first result: "))
# s = int(input("Input your desired result: "))
# day = 1
# print(f"{day} days {n} km")
# while n<s:
#     n*=1.1
#     n=round(n, 2)
#     day+=1
#     print(f"{day} days {n} km")
# print(f"You need {day} days to achieve result!")


