# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле
# Пример процедуры для сортировки списка чисел в порядке убывания, используя алгоритм сортировки выбором:

def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)

numbers = [1, 7, 3, 9, 5]
sorting = sort_list_declarative(numbers)
print(sorting)   
# Вывод: [9, 5, 3, 7, 1]
