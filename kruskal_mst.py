def kruskal_mst(G):
    sort_list = sorted(G, key=lambda x: x[2])
    dicts = {vertex: vertex for vertex in range(6)}
    mst = []

    for edge in sort_list:
        a, b, c = edge
        if dicts[a] != dicts[b]:
            mst.append((a, b, c))
            old_component = dicts[b]
            new_component = dicts[a]
            for vertex, component in dicts.items():
                if component == old_component:
                    dicts[vertex] = new_component

    return mst


with open("MST_input", "r") as input_file:
    graph = []
    for line in input_file:
        a, b, c = map(int, line.split(', '))
        graph.append((a, b, c))

result = kruskal_mst(graph)

with open("MST_output", "w") as output_file:
    for edge in result:
        output_file.write(f"({edge[0]}, {edge[1]}, {edge[2]})\n")
