import lab1


def main():
    groups = lab1.main()
    input_matrix = lab1.input_matrix

    groups = get_operations_by_groups(input_matrix, groups)

    if __name__ == "__main__":
        print_groups(groups)

    optimized_groups = optimize(groups)

    if __name__ == "__main__":
        print("\n\nУточненные группы")
        print_groups(optimized_groups)

    return optimized_groups


def get_operations_by_groups(input_matrix, groups):
    def get_op_by_group(group):
        ops = set()
        for i in group:
            ops.update(input_matrix[i])
        return ops

    return [
        (
            g,
            get_op_by_group(g)
        )
        for g in groups
    ]


def optimize(groups):
    def move(from_index, to_index):
        groups[to_index][0].extend(groups[from_index][0])
        groups[to_index][1].update(groups[from_index][1])
        del groups[from_index]

    def optimize_():
        for i_to, (_, op_to) in enumerate(groups):
            for i_from in range(i_to+1, len(groups)):
                if groups[i_from][1].issubset(op_to):
                    move(i_from, i_to)
                    return True

    while True:
        groups = sorted(groups, key=lambda v: len(v[1]), reverse=True)
        if not optimize_():
            return groups


def print_groups(groups):
    for i, (gr, op) in enumerate(groups):
        print(f"{i+1}: \t {gr} \t {op}")


if __name__ == "__main__":
    main()
