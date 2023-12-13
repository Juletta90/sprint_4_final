# https://contest.yandex.ru/contest/52720/run-report/102553865/ - ����� �������� �������


def how_many_platforms(robot_weight: list, limit: int) -> int:
    """
    ������� ��������� ���-�� �������� ��� ��������� �������:
    1. ��������� ������ ��� ���������� ������ ���� ����������
       1.1. ����� ������� number_robots_max_weight
    2. ������������� ��������� ��������� ����������
    3. ���� � ������ 1 �����, ��������� ��� ���� ���������
    4. ������� ��-� � �������� left_pointer � ���������� ��������� ������
    5. ���� ��������� ��� ������� > limit:
       5.1. ���� ��������� ����� - ��������� �������� ������� ���������.
    6. ���� ��������� ��� ������� <= limit:
       6.1. ��������� ���������, ������� ��-��, ������� ��� ����������
       6.2. ���������� ��������� ������, �������� ������ ����������
    """

    robot_weight_sorted: list = sorted(robot_weight)
    number_of_platforms, robot_weight_sorted = (number_robots_max_weight
                                                (robot_weight_sorted, limit))
    left_pointer = 0
    right_pointer = len(robot_weight_sorted) - 1

    while left_pointer <= right_pointer:
        if left_pointer == right_pointer:
            number_of_platforms += 1
            if len(robot_weight_sorted) == 1:
                break
            #robot_weight_sorted.pop(left_pointer)
            left_pointer = 0
            right_pointer = len(robot_weight_sorted) - 1
        elif (robot_weight_sorted[left_pointer] +
              robot_weight_sorted[right_pointer] > limit):
            right_pointer -= 1

        elif (robot_weight_sorted[left_pointer] +
              robot_weight_sorted[right_pointer] <= limit):

            number_of_platforms += 1
            #robot_weight_sorted.pop(right_pointer)
            #robot_weight_sorted.pop(left_pointer)
            left_pointer = 0
            right_pointer = len(robot_weight_sorted) - 1

    return number_of_platforms


def number_robots_max_weight(robot_weight_sorted: list, limit: int) -> tuple[
    int, list]:
    """
     ������� ��������� ���������� �������,
     ��� ��� ����� ���������������� ��������� (limit)
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
