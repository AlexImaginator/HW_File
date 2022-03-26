from CookPlaner import *
from FileCompiller import *


# Задачи 1 и 2
print('Задачи 1 и 2')
person_count = 5
dishes_list = ['Омлет', 'Утка по-пекински', 'Запеченный картофель']
planner = CookPlanner('recipes.txt')
planner.print_shop_list(dishes_list, person_count)
print()

# Задача 3
print('Задача 3')
filecompiller = FileCompiller('1.txt', '2.txt', '3.txt')
filecompiller.compile_files('compile_result.txt')
