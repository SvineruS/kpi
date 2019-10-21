# todo че бля дальше с графом делать в душе не ебу

import lab1
import lab2


def main():
    groups = lab2.main()
    input_matrix = lab1.input_matrix

    for g in groups:
        make_graph(g, input_matrix)
        break


def make_graph(group, input_matrix):
    def parse_row(row):
        row_indexes = [op.index(r) for r in row]
        for i in range(len(row)-1):
            el1 = row_indexes[i]
            el2 = row_indexes[i+1]
            graph[el1][el2] = 1

    gr, op = group
    op = list(sorted(op))
    graph = zeros(len(op))

    print(*op, sep='\n')

    for i in gr:
        row = input_matrix[i]
        print(row)
        parse_row(row)

    print(*graph, sep='\n')


def zeros(n):
    return [[0] * n for i in range(n)]


if __name__ == "__main__":
    main()
