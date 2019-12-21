import lab1
import lab5
from itertools import groupby
from statistics import mean


def main():
    input_matrix = lab1.input_matrix
    modules = lab5.main()

    #
    # todo в этой лабе надо бы сделать оптимизацию (наверное), но мне повезло и нихуя делать не надо
    #
    modules_in_details = [get_modules_in_detail(detail, modules) for detail in input_matrix]

    if __name__ == '__main__':
        print("Количество модулей для деталей:")
        for i, count in enumerate(modules_in_details):
            print(f"{i} деталь = {count}")
        print("Среднее кол-во модулей: ", mean(modules_in_details))


def get_modules_in_detail(detail, modules):
    ms = [lab5.find_module_with_element(modules, element) for element in detail]
    return len(list(groupby(ms)))  # groupby убирает повторы подряд


if __name__ == '__main__':
    main()
