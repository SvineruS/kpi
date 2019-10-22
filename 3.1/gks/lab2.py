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
    def optimize_(groups_, index):
        groups_[0][0].extend(groups_[index][0])
        groups_[0][1].update(groups_[index][1])
        del groups_[index]

    while True:
        groups = sorted(groups, key=lambda v: len(v[1]), reverse=True)

        for i, (_, op) in enumerate(groups[1:]):
            if op.issubset(groups[0][1]):
                optimize_(groups, i+1)
                break

        return groups


def print_groups(groups):
    for i, (gr, op) in enumerate(groups):
        print(f"{i+1}: \t {gr} \t {op}")


if __name__ == "__main__":
    main()
