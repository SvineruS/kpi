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

    matrix1 = merge_matrix(user_input)
    all_operations = get_all_operations(matrix1)
    matrix2 = matrix_by_operations(matrix1, all_operations)

    similarity = get_similarity(matrix2)
    similarity = dict(sorted(similarity.items(), key=lambda i: -i[1]))
    groups = get_groups(similarity)

    print_m1(matrix1)
    print_operations(all_operations)
    print_m2(matrix2, all_operations)
    print_similarity(similarity)
    print(groups)


def get_user_input():
    print("enter matrix:")
    input_matrix = []
    for i in range(-1):
        inp = input(f"{i+1}: ")
        if not inp:
            break
        input_matrix.append(inp)
    return input_matrix


def merge_matrix(user_input):
    return set(tuple(inp.split(" ")) for inp in user_input)


def get_all_operations(matrix):
    operations = set()
    for row in matrix:
        for i in row:
            operations.add(i)
    return list(sorted(operations))


def matrix_by_operations(matrix1, all_operations):
    return [
        [
            operation in row
            for operation in all_operations
        ]
        for row in matrix1
    ]


def get_similarity(matrix):

    def get_rows_similarity(r1, r2):
        cnt = 0
        for i in range(len(r1)):
            if r1[i] == r2[i]:
                cnt += 1
        return cnt

    similarity = {}

    for index in range(len(matrix) - 1):
        row1 = matrix[index]
        row2 = matrix[index+1]

        similarity[(index, index+1)] = get_rows_similarity(row1, row2)

    return similarity


def get_groups(similarity):
    groups = []
    banned_rows = set()
    for (r1, r2), s in similarity.items():
        if r1 in banned_rows or r2 in banned_rows:
            continue
        groups.append((r1, r2))
        banned_rows.add(r1)
        banned_rows.add(r2)
    return groups


def print_m1(matrix):
    print("Матрица:")
    for i, r in enumerate(matrix):
        print(f'{i}:', *r)
    print()


def print_operations(operations):
    print("Возможные операции: " + ", ".join(operations))
    print()


def print_m2(matrix, operations):
    print("Матрица по операциям:")
    print('  ', *operations, sep=' ')
    for i, row in enumerate(matrix):
        print(i, end='  ')
        for el in row:
            print("+" if el else "-", " ", end='')
        print()
    print()


def print_similarity(similarity):
    print("Подобность строк: ")
    for (r1, r2), s in similarity.items():
        print(f"{r1} и {r2} = {s}")
    print()


main()
