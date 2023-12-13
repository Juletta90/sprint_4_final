#!/usr/bin/python
# -*- coding: utf-8 -*-
# https://contest.yandex.ru/contest/52720/run-report/102553865/ - номер успешной посылки


# Для алгоритма нам не нужно удалять элементы из списка. Достаточно завести два
# курсора, левый и правый, и двигаться по исходному отсортированному
# списку(sorted), переставляя курсоры на каждой итерации.

# Что получится:
# Цикл будет продолжать пока левый курсор не больше правого.
# Если сумма элемента, на который указывает левый курсор и элемента на который
# указывает правый курсор меньше или равны лимиту, то обновляем счетчик
# и сдвигаем курсоры. Иначе сдвигаем только правый и также обновляем
# счетчик и переходим к следующей итерации.



def how_many_platforms(robot_weight: list, limit: int) -> int:
    """
    Функция вычисляет кол-во платформ для перевозки роботов:
    1. Сортируем список для применения метода двух указателей
       1.1. Вызов функции number_robots_max_weight
    2. Устанавливаем начальное положение указателей
    3. Если в списке 1 робот, добавляем для него платформу
    4. Удаляем эл-т с индексом left_pointer и выставляем указатели заново
    5. Если суммарный вес роботов > limit:
       5.1. надо уменьшить сумму - уменьшаем значение правого указателя.
    6. Если суммарный вес роботов <= limit:
       6.1. добавляем платформу, удаляем эл-ты, которые уже подсчитали
       6.2. выставляем указатели заново, интервал поиска уменьшился
    """

    robot_weight_sorted: list = sorted(robot_weight)
    number_of_platforms, robot_weight_sorted = (number_robots_max_weight
                                                (robot_weight_sorted, limit))
    left_pointer = 0
    right_pointer = len(robot_weight_sorted) - 1

    while left_pointer < right_pointer:
        if left_pointer == right_pointer:
            number_of_platforms += 1
            if len(robot_weight_sorted) == 1:
                break
            #robot_weight_sorted.pop(left_pointer)
            #left_pointer = 0
            #right_pointer = len(robot_weight_sorted) - 1
            #left_pointer += 1
            #right_pointer -= 1

        elif (robot_weight_sorted[left_pointer] +
              robot_weight_sorted[right_pointer] > limit):
            right_pointer -= 1
            number_of_platforms += 1

        elif (robot_weight_sorted[left_pointer] +
              robot_weight_sorted[right_pointer] <= limit):

            number_of_platforms += 1
            #robot_weight_sorted.pop(right_pointer)
            #robot_weight_sorted.pop(left_pointer)
            #left_pointer = 0
            #right_pointer = len(robot_weight_sorted) - 1
            left_pointer += 1
            right_pointer -= 1

    return number_of_platforms


def number_robots_max_weight(robot_weight_sorted: list, limit: int) -> tuple[
    int, list]:
    """
     Функция вычисляет количество роботов,
     чей вес равен грузоподъемности платформы (limit)
     """
    count = 0
    result_list = robot_weight_sorted
    for index in range(len(robot_weight_sorted)-1, 0, -1):
        if robot_weight_sorted[index] == limit:
            count += 1
            #result_list.pop(index)
        else:
            break
    return count, result_list


def main():
    robot_weight = [int(i) for i in input().split()]
    limit = int(input())
    print(how_many_platforms(robot_weight, limit))


if __name__ == '__main__':
    main()
