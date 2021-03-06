import lab1
import lab4
from collections import Counter


def main():
    input_matrix = lab1.input_matrix
    modules = lab4.main()

    first, last = get_firstlast_operations(input_matrix, modules)

    if __name__ == '__main__':
        print("Операции: ")
        print(*input_matrix, sep='\n')
        print("\nМодули: ")
        print(*modules, sep='\n')

        print(f"\nМодуль, в котором содержится {first}, нужно поставить в начало")
        print(f"Модуль, в котором содержится {last}, нужно поставить в конец\n")

    swap_modules(modules, first, 0)
    swap_modules(modules, last, -1)

    if __name__ == '__main__':
        print("Оптимизированные модули: ")
        print(*modules, sep='\n')

    return modules


def get_firstlast_operations(input_matrix, modules):
    first_operations = Counter()
    last_operations = Counter()

    for operation in input_matrix:
        first_operations[operation[0]] += 1
        last_operations[operation[-1]] += 1

    first = first_operations.most_common()[0][0]
    lasts = last_operations.most_common()
    last = lasts.pop(0)[0]

    while find_module_with_element(modules, first) == find_module_with_element(modules, last):
        last = lasts.pop(0)[0]

    return first, last


def swap_modules(modules, element, to_pos):
    from_pos = find_module_with_element(modules, element)
    modules[from_pos], modules[to_pos] = modules[to_pos], modules[from_pos]


def find_module_with_element(modules, element):
    for module_id, module in enumerate(modules):
        if element in module:
            return module_id


if __name__ == '__main__':
    main()
