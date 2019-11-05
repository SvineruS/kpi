import lab1
import lab2


def main():
    lab2_output = lab2.main()
    input_matrix = lab1.input_matrix

    modules_by_group = [
        get_modules(group, input_matrix)
        for group in lab2_output
    ]

    optimized_modules = optimize_modules(modules_by_group)

    if __name__ == "__main__":
        print_modules_by_group(modules_by_group)
        print_optimized_modules(optimized_modules)


def get_modules(group, input_matrix):
    graph = Graph.create_from_group(group, input_matrix)
    graph.optimize()
    return [tuple(i) for i in graph.names]


def optimize_modules(modules_by_group):
    modules = [item for sublist in modules_by_group for item in sublist]
    modules = set(modules)
    modules = sorted(modules, key=lambda i: len(i))
    return modules


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
        print(self.names)
        print(*self.matrix, sep='\n')

    def find_cycle(self, visited):
        for index, is_adj in enumerate(self.matrix[visited[-1]]):
            if is_adj:
                if index in visited:
                    return visited
                return self.find_cycle(visited + [index])

    def find_chain(self, visited):
        for index, is_adj in enumerate(self.matrix[visited[-1]]):
            if len(visited) > 2 and self.matrix[visited[0]][visited[-1]]:
                return visited
            if is_adj and index not in visited:
                return self.find_chain(visited + [index])

    def merge_vertices(self, vertices):
        vertices = list(sorted(vertices, reverse=True))
        merge_to = vertices.pop(0)

        for vi in vertices:
            self.names[merge_to].extend(self.names[vi])

            for i in range(len(self.matrix)):
                self.matrix[merge_to][i] = self.matrix[merge_to][i] or self.matrix[vi][i]
                self.matrix[i][merge_to] = self.matrix[i][merge_to] or self.matrix[i][vi]
                self.matrix[i][i] = 0

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

        while True:
            for i in range(len(self.matrix)):
                if any((
                    merge_if_(self.find_cycle([i])),
                    merge_if_(self.find_chain([i]))
                )):
                    break
            break


# region utils and print

def zeros(n):
    return [[0] * n for _ in range(n)]


def print_modules_by_group(modules_by_group):
    print("Модули по группам")
    for i, ms in enumerate(modules_by_group):
        print(f"Группа {i}:")
        for m in ms:
            print('\t\t', ', '.join(m))


def print_optimized_modules(optimized_modules):
    print("\n\nУточненные модули")
    for i in optimized_modules:
        print(', '.join(i))

# endregion


if __name__ == "__main__":
    main()
