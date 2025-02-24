# Рядки (Strings):
# Напишіть функцію, яка приймає рядок і повертає його довжину.
#
# def str_len(string):
#     return print(len(string))
#
# sentence = "11 children go for a walk"
# str_len(sentence)

# Створіть функцію, яка приймає два рядки і повертає об'єднаний рядок.
#
# def sum_str(string1, string2):
#     return print(string1 + " " + string2)
#
# string1 = input("Enter string 1: ")
# string2 = input("Enter string2: ")
#
# sum_str(string1, string2)
#
# Числа (Int/float):
# Реалізуйте функцію, яка приймає число і повертає його квадрат.
#
# def square(number):
#     return print(pow(number, 2))
#
# try:
#     num = int(input("Enter number : "))
#     square(num)
# except ValueError:
#     print("Enter numbers only")
# except Exception as e:
#     print(e)

# Створіть функцію, яка приймає два числа і повертає їхню суму.
#
# def sum(num1, num2):
#         return print(num1 +num2)
#
# sum(5, 6)

# Створіть функцію яка приймає 2 числа типу int, виконує операцію ділення та повертає чілу частину і залишок.
#
# def devision(num1, num2):
#     return print(f"{num1 // num2}, {num1 % num2}")
#
# devision(20, 7)
#
# Списки (Lists):
# Напишіть функцію для обчислення середнього значення списку чисел.
# a = [8, 9, 7, 5, 3]
# b= sum(a) / len(a)
# print(b)

# Реалізуйте функцію, яка приймає два списки і повертає список, який містить спільні елементи обох списків.
#
# list1 = [8, 6, 5, 0, 3, 1]
# list2 = [7, 0, 8, 2, 9, 3]
# list3 = list(set(list1).intersection(list2))
# print(list3)

# Словники (Dictionaries):
# Створіть функцію, яка приймає словник і виводить всі ключі цього словника.
# person = {"math" : "5", "geography" : "4", "literature": "3"}
# for key in schedule :
#     print(key, " ")

# Реалізуйте функцію, яка приймає два словники і повертає новий словник, який є об'єднанням обох словників.
#
# person1 = {"math": "5", "geography": "4", "literature": "3"}
# person2 = {"math": "5", "phisics": "2", "literature": "4"}
# v1
# person1.update(person2)
# print(person1)
# v2
# sum = person1 | person2
# print(sum)

# Множини (Sets):
# Напишіть функцію, яка приймає дві множини і повертає їхнє об'єднання.

# a = {5, 6, 8, 9, 3, 4,}
# b = {6, 7, 7, 1}
# c = a | b
# print(c)

# Створіть функцію, яка перевіряє, чи є одна множина підмножиною іншої.
# #
# set1 = {5, 6, 8, 9, 3, 4,}
# set2 = {8, 9,4}
#
# if set2 not in set1:
#     print("set2 is part of the set1")
# else:
#     print("set2 is not the part of the set1")

# Умовні вирази та цикли:
# Реалізуйте функцію, яка приймає число і виводить "Парне", якщо число парне, і "Непарне", якщо непарне.
#
# num = int(input("Enter number: "))
#
# if num % 2 == 0 :
#     print("Парне")
# else:
#     print("Непарне")

# Створіть функцію, яка приймає список чисел і повертає новий список, що містить тільки парні числа.
# list = [3, 4, 5, 6, 9]
# for i in list:
#         if i % 2 == 0:
#                 print(i, end = " ")