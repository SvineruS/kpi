# todo че бля дальше с графом делать в душе не ебу

import lab1
import lab2


def main():
    groups = lab2.main()
    input_matrix = lab1.input_matrix

    for g in groups:
        graph, op = make_graph(g, input_matrix)
        split_modules(graph, op)
        break


def make_graph(group, input_matrix):
    gr, op = group
    op = list(sorted(op))
    graph = zeros(len(op))

    for row_index in gr:
        row = input_matrix[row_index]
        row_indexes = [op.index(r) for r in row]
        for i in range(len(row) - 1):
            el1 = row_indexes[i]
            el2 = row_indexes[i + 1]
            graph[el1][el2] = 1

    return graph, op


def split_modules(graph, op):
    pass



def zeros(n):
    return [[0] * n for _ in range(n)]


if __name__ == "__main__":
    main()
