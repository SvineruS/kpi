from tabulate import tabulate  # pip3 install tabulate


def main():
    # user_input = get_user_input()
    user_input = [
        "Т1 Ф1 Т4 С1 С2",
        "Т1 Ф1 Ф2 Т4 С1 С2 Т2 Т3",
        "Т2 Т3 Ф1 Ф2 Р1 Т4 С1 С2",
        "Т4 С1 С2 Ф1 Ф2",
        "Т3 Т4 С1 С2 Ф1 Т5",
        "Т1 Т4 С1 С2 Ф1 Т5",
        "Т1 Т2 Т4 С1 С2 Ф2 Т5",

        "Т2 Т3 Т4 С1 С2 Р1 Ф1 Ф2",
        "Ф2 Ф3 С3 Т2 Т3 Т4 С1 С2",
        "Ф2 Т4 С1 С2 Т1",
        "Т1 Ф1 Ф2 Т4 С1 С2 Т2 Т3",
        "Т1 Ф1 Т4 С1 С2",
        "Т2 Т3 Ф1 Ф2 Р1 Т4 С1 С2",
        "Т4 С1 С2 Ф1 Ф2"
    ]

    input_matrix = parse_input(user_input)
    all_operations = get_all_operations(input_matrix)
    operations_match_matrix = matrix_by_operations(input_matrix, all_operations)
    similarity = get_similarity(operations_match_matrix)
    groups = get_groups(similarity)

    print_input_matrix(input_matrix)
    print_operations(all_operations)
    print_op_match_matrix(operations_match_matrix, all_operations)
    print_similarity(similarity, len(operations_match_matrix))
    print_groups(groups, similarity)


def get_user_input():
    print("enter matrix:")
    input_matrix = []
    for i in range(-1):
        inp = input(f"{i+1}: ")
        if not inp:
            break
        input_matrix.append(inp)
    return input_matrix


def parse_input(user_input):
    return [tuple(inp.split(" ")) for inp in user_input]


def get_all_operations(matrix):
    operations = set(el for row in matrix for el in row)  # сет из всех элементов
    return list(sorted(operations))


def matrix_by_operations(matrix, all_operations):
    # матрица со столбацами all_operations, строками из введенной матрици и True или False на пересечении
    return [
        [
            operation in row
            for operation in all_operations     # 2) элементы массива со всеми операциями
        ]
        for row in matrix                       # 1) строки входной матрицы
    ]


def get_similarity(matrix):
    def get_rows_similarity(r1, r2):  # подобность 2х отдельных строк
        return len([1 for i in range(len(r1)) if r1[i] == r2[i]])

    similarity = {}
    for i1 in range(len(matrix) - 1):  # перебор всех сочитаний (как в теории вероятности) индексов
        for i2 in range(i1+1, len(matrix)):  # как же хорошо что хоть сюда я не засунул List comprehensions лол
            similarity[i1, i2] = get_rows_similarity(matrix[i1], matrix[i2])

    return similarity


def make_group(similarity, x, y):
    group = {x, y}
    for (x1, y1), s in similarity.items():
        if x1 in group or y1 in group:
            if s == similarity[(x, y)]:
                group.update([x1, y1])

    new_similarity = {}
    for (x1, y1), s in similarity.items():
        if x1 not in group and y1 not in group:
            new_similarity[(x1, y1)] = s

    return list(sorted(group)), new_similarity


def get_groups(similarity):
    similarity = dict(sorted(similarity.items(), key=lambda i: i[1]))
    groups = []

    while similarity:
        (x, y), s = list(similarity.items()).pop()
        g, similarity = make_group(similarity, x, y)
        if not g:
            break
        groups.append(g)

    return groups


# region print

def print_input_matrix(matrix):
    print("Входные данные:")
    for i, r in enumerate(matrix):
        print(f'{i}:', *r)
    print()


def print_operations(operations):
    print("Возможные операции: " + ", ".join(operations) + "\n")


def print_op_match_matrix(matrix, operations):
    print("Матрица соответсвий операциям:")
    table = [['', *operations]]
    for i, row in enumerate(matrix):
        table.append([i, *["+" if el else "-" for el in row]])
    print(tabulate(table, tablefmt="fancy_grid"))


def print_similarity(similarity, size):
    print("Подобность строк: ")
    table = [
        [
            '-' if y >= x else similarity[(y, x)]
            for y in range(size)
        ]
        for x in range(size)
    ]
    for i, r in enumerate(table):
        r.insert(0, f'{i}:')
    table.insert(0, ['*']+list(range(size)))
    print(tabulate(table, tablefmt="fancy_grid"))


def print_groups(groups, similarity):
    print("Группы: ")
    for i, g in enumerate(groups):
        s = similarity[tuple(g)[:2]]
        print(f"Группа {i+1} = {{", end='')
        print(*g, sep=', ', end='')
        print(f'}} по {s}')


# endregion print

main()
