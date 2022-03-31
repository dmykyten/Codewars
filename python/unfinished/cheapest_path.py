#https://www.codewars.com/kata/5abeaf0fee5c575ff20000e4
def cheapest_path(t, start, finish):
    graph = []

    def matrix_to_graph():
        for y, row in enumerate(t):
            for x, item in enumerate(row):
                [graph.append(((y, x), (y, x_elem), t[y][x] + t[y][x_elem]))
                 for x_elem in range(x - 1, x + 2)
                 if x_elem in range(len(row)) and x_elem != x]
                [graph.append(((y, x), (y_elem, x), t[y][x] + t[y_elem][x]))
                 for y_elem in range(y - 1, y + 2)
                 if y_elem in range(len(t) and y_elem != y)]

    def move():
        start_connections = [elem for elem in graph if start in elem]




cheapest_path([[1, 4, 1],
               [1, 9, 1],
               [1, 1, 1]], (0, 0), (0, 2))
