# todo


optimized_modules = optimize_modules(modules_by_group)
print_optimized_modules(optimized_modules)



def optimize_modules(modules_by_group):
    modules = [item for sublist in modules_by_group for item in sublist]
    modules = set(modules)
    modules = sorted(modules, key=lambda i: len(i))
    return modules


def print_optimized_modules(optimized_modules):
    print("\n\nУточненные модули: ")
    for i in optimized_modules:
        print(', '.join(i))
