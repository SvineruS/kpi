import lab1
import lab5
import networkx as nx
import matplotlib.pyplot as plt


def main():
    input_matrix = lab1.input_matrix
    ordered_modules = lab5.main()

    make_graph(input_matrix, ordered_modules)


def make_graph(input_matrix, modules):
    names = [''.join(m) for m in modules]
    edges_green, edges_red = [], []
    rows_by_modules = {i: set() for i, _ in enumerate(modules)}

    for row_index, row in enumerate(input_matrix):
        modules_index = [lab5.find_module_with_element(modules, element) for element in row]
        for i in modules_index:
            rows_by_modules[i].add(row_index)

        for i in range(len(row) - 1):
            el1 = modules_index[i]
            el2 = modules_index[i + 1]
            edge = (names[el1], names[el2])

            if el1 > el2:
                edges_green.append(edge)
            else:
                edges_red.append(edge)

    graph = edges_green + edges_red

    G = nx.DiGraph()
    G.add_edges_from(graph)

    pos = {n: [i, 0] for i, n in enumerate(names)}

    nx.draw_networkx_nodes(G, pos, node_shape='s', node_color='white', edgecolors='gray', node_size=3500)  # квадраты
    nx.draw_networkx_labels(G, pos, font_size=7)                                                           # надписи
    nx.draw_networkx_edges(G, pos, edgelist=edges_green, connectionstyle='arc3,rad=0.5', edge_color='g')  # зеленые дуги
    nx.draw_networkx_edges(G, pos, edgelist=edges_red,   connectionstyle='arc3,rad=0.5', edge_color='r')  # красные дуги

    for mod, rows in rows_by_modules.items():
        rows = map(str, sorted(rows))
        plt.plot((mod-0.3, mod-0.3), (0.03, 0.2), color='k', linewidth=0.5)  # верт. линия
        plt.text(mod-0.25, 0.1, '\n'.join(rows), fontsize=6)  # надпись

    plt.show()


if __name__ == '__main__':
    main()
