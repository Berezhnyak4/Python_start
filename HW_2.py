"""1. Создать список и заполнить его элементами различных типов данных.
 Реализовать скрипт проверки типа данных каждого элемента. Использовать
  функцию type() для проверки типа. Элементы списка можно не запрашивать
   у пользователя, а указать явно, в программе."""
print("1 qwest")
l = [0,1,2,3,"one",None,False,2.3,(1,2,3),{1:"1"}]
for i in l:
    print(type(i))

"""2. Для списка реализовать обмен значений соседних элементов, т.е. 
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При 
нечетном количестве элементов последний сохранить на своем месте. Для
 заполнения списка элементов необходимо использовать функцию input()."""
# print("2 qwest")#  работает отдельно от 3
# a =list(map(int, input( "Введите последовательность чисел через пробел: ").split()))
# k=1
# print(a)
# for i in range(0,len(a)+1,2):
#     a[i], a[k] =a[k], a[i]
#     k+=2
#
#     print(a)
"""3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить
 к какому времени года относится месяц (зима, весна, лето, осень). 
 Напишите решения через list и через dict."""
print("3 qwest")
month = int(input("Введите номер месяца в виде целого числа от 1 до 12: "))
m = ["зима", "зима", "весна", "весна", "весна", "лето", "лето", "лето", "осень", "осень", "осень", "зима"]
print(f'Это {m[month - 1]}')
m_dict = {1:"winter", 2:"winter",12:"winter", 3:"Spring", 4:"Spring", 5:"Spring", 6:"Summer", 7:"Summer", 8:"Summer", 9:"Autumn", 10:"Autumn", 11:"Autumn"}
print(f'This is {m_dict.get(month)}')
print("4 qwest")
"""4. Пользователь вводит строку из нескольких слов, разделённых
 пробелами. Вывести каждое слово с новой строки. Строки необходимо 
 пронумеровать. Если в слово длинное, выводить только первые 10 букв 
 в слове."""
n=0
stroka = input("Введитее слова через пробел: ").split()
for i in stroka:
        print(f'{n+1}.{i[0:10]}')
        n+=1
"""5. Реализовать структуру «Рейтинг», представляющую собой не 
возрастающий набор натуральных чисел. У пользователя необходимо
 запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
  с одинаковыми значениями, то новый элемент с тем же значением должен 
  разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например,
 my_list = [7, 5, 3, 3, 2]."""
print("5 qwest")

my_list = [7, 5, 5, 3, 3, 3, 2]
a = int(input("Введите число: "))

r=False
for i in range(len(my_list)-1,-1,-1):
    if my_list[i] >= a:
        my_list.insert(i+1,a)
        r=True
        break
if not r:
    my_list.insert(0,a)

my_list.reverse()

print(my_list)
"""6. * Реализовать структуру данных «Товары». Она должна представлять 
собой список кортежей. Каждый кортеж хранит информацию об отдельном 
товаре. В кортеже должно быть два элемента — номер товара и словарь с 
параметрами (характеристиками товара: название, цена, количество,
 единица измерения). Структуру нужно сформировать программно, т.е. 
 запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором 
каждый ключ — характеристика товара, например название, а значение — 
список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}"""
print("6 qwest")
print('Для выхода введите "конец"')
cnt =1
list =[]
while True:
    dict_n = {"Название": None, "цена":None, "колличество":None, "“ед”: [“шт.”]":None}
    name = input("Введите название товара: ")
    if name == "конец":
        break
    dict_n["Название"] = name
    print(dict_n)
    cost= input("Введите цену товара: ")
    if cost == "конец":
        break
    dict_n["цена"] = cost
    print(dict_n)
    number = input("Введите колличество товара: ")
    if number == "конец":
        break
    dict_n["колличество"] = number
    print(dict_n)
    ed = input("Введите “ед”: [“шт.”]: ")
    if ed == "конец":
        break
    dict_n["“ед”: [“шт.”]"] = ed
    print(dict_n)
    list.append((cnt,dict_n))
    cnt+=1
print(list)

sborka={"Название":[], "цена":[], "колличество":[], "“ед”: [“шт.”]":[]}
for nomer in list:
    kluch = nomer[1]
    for znach in kluch.keys():
        if sborka[znach].count(kluch[znach]) == 0:
            sborka[znach].append(kluch[znach])
print(sborka)


