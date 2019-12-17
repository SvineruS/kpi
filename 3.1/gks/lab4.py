import lab3


def main():
    lab3_output = lab3.main()

    optimized_modules = optimize_modules(lab3_output)

    if __name__ == "__main__":
        lab3.print_modules_by_group(lab3_output)
        print_optimized_modules(optimized_modules)

    return optimized_modules


def optimize_modules(modules_by_group):
    modules = [list(item) for sublist in modules_by_group for item in sublist]
    modules = sorted(modules, key=lambda i: len(i))

    def exist(operation, start_index):
        for i in modules[start_index+1:]:
            if operation in i:
                return True

    for i, m in enumerate(modules):
        modules[i] = [m for m in modules[i] if not exist(m, i)]

    return list(filter(None, modules))


def print_optimized_modules(optimized_modules):
    print("\n\nУточненные модули: ")
    for i in optimized_modules:
        print(', '.join(i))


if __name__ == "__main__":
    main()