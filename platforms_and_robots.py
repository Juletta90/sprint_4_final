# номер успешной посылки
# https://contest.yandex.ru/contest/52720/run-report/102787651/

def how_many_platforms(robot_weight: list, limit: int) -> int:
    """
    Функция вычисляет кол-во платформ для перевозки роботов:
    1. Сортируем список для применения метода двух указателей
    2. Устанавливаем начальное положение указателей
    3. Если в списке 1 робот, добавляем для него платформу
    4. Если суммарный вес роботов <= limit:
        4.1 обновляем счетчик
        4.2 сдвигаем курсоры
    5. Если суммарный вес роботов > limit:
       5.1 надо уменьшить сумму - уменьшаем значение правого указателя.
       5.2 обновляем счетчик
    """
    number_of_platforms: int = 0
    robot_weight_sorted: list = sorted(robot_weight)

    left_pointer: int = 0
    right_pointer: int = len(robot_weight_sorted) - 1

    while left_pointer <= right_pointer:

        if left_pointer == right_pointer:
            number_of_platforms += 1
            break

        if (robot_weight_sorted[left_pointer] +
                robot_weight_sorted[right_pointer] <= limit):
            number_of_platforms += 1
            left_pointer += 1
            right_pointer -= 1

        elif (robot_weight_sorted[left_pointer] +
              robot_weight_sorted[right_pointer] > limit):
            right_pointer -= 1
            number_of_platforms += 1

    return number_of_platforms


def main():
    robot_weight: list = [int(i) for i in input().split()]
    limit: int = int(input())
    print(how_many_platforms(robot_weight, limit))


if __name__ == '__main__':
    main()
