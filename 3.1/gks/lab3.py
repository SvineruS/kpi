import lab1
import lab2


def main():
    lab2_output = lab2.main()
    input_matrix = lab1.input_matrix

    modules_by_group = [
        get_modules(group, input_matrix)
        for group in lab2_output
    ]

    if __name__ == "__main__":
        print_operations_by_group(lab2_output, input_matrix)
        print_modules_by_group(modules_by_group)

    return modules_by_group


def get_modules(group, input_matrix):
    graph = Graph.create_from_group(group, input_matrix)
    # graph.print()
    graph.optimize()
    return graph.names


class Graph:
    @staticmethod
    def create_from_group(group, input_matrix):
        group_rows, operations = group
        names = list(sorted(operations))
        matrix = zeros(len(names))

        for row_index in group_rows:
            row = input_matrix[row_index]
            row_indexes = [names.index(r) for r in row]
            for i in range(len(row) - 1):
                el1 = row_indexes[i]
                el2 = row_indexes[i + 1]
                matrix[el1][el2] = 1

        names = [[i] for i in names]
        return Graph(matrix, names)

    def __init__(self, matrix, names):
        self.matrix = matrix
        self.names = names

    def print(self):
        for i in self.names:
            print('-'.join(i))
        print(*self.matrix, sep='\n')

    def find_cycle(self, visited):
        for index, is_adj in enumerate(self.matrix[visited[-1]]):
            if is_adj and len(visited) >= 2 and index == visited[0]:
                return visited
            if is_adj and index not in visited:
                return self.find_cycle(visited + [index])

    def find_chain(self, visited):
        for index, is_adj in enumerate(self.matrix[visited[-1]]):
            if len(visited) > 2 and self.matrix[visited[0]][visited[-1]]:
                return visited
            if is_adj and index not in visited:
                return self.find_chain(visited + [index])

    def merge_vertices(self, vertices):
        merge_to = vertices.pop(0)

        for vi in vertices:
            self.names[merge_to].extend(self.names[vi])

            for i in range(len(self.matrix)):
                self.matrix[merge_to][i] = self.matrix[merge_to][i] or self.matrix[vi][i]
                self.matrix[i][merge_to] = self.matrix[i][merge_to] or self.matrix[i][vi]
                self.matrix[i][i] = 0

        vertices = list(sorted(vertices, reverse=True))
        for vi in vertices:
            del self.matrix[vi]
            del self.names[vi]
            for i in range(len(self.matrix)):
                del self.matrix[i][vi]

    def optimize(self):
        def merge_if_(vertices):
            if vertices:
                self.merge_vertices(vertices)
                return True

        def optimize_():
            for i in range(len(self.matrix)):
                if merge_if_(self.find_cycle([i])) or\
                   merge_if_(self.find_chain([i])):
                    return True

        while optimize_():
            pass

# region utils and print

def zeros(n):
    return [[0] * n for _ in range(n)]


def print_operations_by_group(groups, input_matrix):
    print('Операции в группе: ')
    for i, group in enumerate(groups):
        print(f"Группа {i}:")
        for row_index in group[0]:
            row = input_matrix[row_index]
            print('\t\t', ', '.join(row))


def print_modules_by_group(modules_by_group):
    print("\n\nМодули в группах:")
    for i, ms in enumerate(modules_by_group):
        print(f"Группа {i}:")
        for m in ms:
            print('\t\t', ', '.join(m))

# endregion


if __name__ == "__main__":
    main()
