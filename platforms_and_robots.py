# номер успешной посылки
# https://contest.yandex.ru/contest/52720/run-report/102889342/

def how_many_platforms(robot_weight: list, limit: int) -> int:
    """
    Функция возвращает количество платформ для перевозки роботов.

        Параметры:
            robot_weight (list): массив целых чисел - вес отдельных роботов
            limit (int): целое число - грузоподъёмность платформы

        Возвращаемое значение:
            number_of_platforms (int): целое число - количество платформ
    """
    number_of_platforms: int = 0
    robot_weight_sorted: list = sorted(robot_weight)

    left_pointer: int = 0
    right_pointer: int = len(robot_weight_sorted) - 1

    while left_pointer <= right_pointer:

        if (robot_weight_sorted[left_pointer] +
                robot_weight_sorted[right_pointer] <= limit):
            number_of_platforms += 1
            left_pointer += 1
            right_pointer -= 1
        else:
            right_pointer -= 1
            number_of_platforms += 1

    return number_of_platforms


def main():
    robot_weight: list[int] = [int(i) for i in input().split()]
    limit: int = int(input())
    print(how_many_platforms(robot_weight, limit))


if __name__ == '__main__':
    main()
