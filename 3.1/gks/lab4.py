import lab3


def main():
    lab3_output = lab3.main()

    sorted_modules = sort_modules(lab3_output)
    # optimized_modules = optimize_modules(sorted_modules)

    if __name__ == "__main__":
        lab3.print_modules_by_group(lab3_output)
        print(*sorted_modules, sep='\n')
        print_optimized_modules(optimized_modules)


def sort_modules(modules_by_group):
    modules = [list(item) for sublist in modules_by_group for item in sublist]
    modules = sorted(modules, key=lambda i: len(i))
    return modules


def optimize_modules(modules):

    def exist(operation, start_index):
        for i in modules[start_index:]:
            if operation in i:
                return True

    for i, m in enumerate(modules):
        for j, op in enumerate(m):
            if exist(op, i):
                del m[j]

    return list(filter(None, modules))


def print_optimized_modules(optimized_modules):
    print("\n\nУточненные модули: ")
    for i in optimized_modules:
        print(', '.join(i))





if __name__ == "__main__":
    main()