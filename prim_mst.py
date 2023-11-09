import heapq


def prim_mst(graph):
    n = len(graph)
    mst = []
    visited = [False] * n
    heap = []

    start_node = 2
    visited[start_node] = True

    for edge in graph:
        u, v, weight = edge
        heapq.heappush(heap, (weight, u, v))

    while heap:
        weight, u, v = heapq.heappop(heap)

        if visited[v]:
            continue

        mst.append((u, v, weight))
        visited[v] = True

        for edge in graph:
            if not visited[edge[1]]:
                u, w, weight = edge
                heapq.heappush(heap, (weight, u, w))

    return mst


with open("MST_input", "r") as input_file:
    lines = input_file.read().splitlines()

input_data = []
for line in lines:
    parts = line.split(',')
    a, b, c = map(int, parts)
    input_data.append((a, b, c))

MST = prim_mst(input_data)

with open("MST_output", "w") as output_file:
    for edge in MST:
        output_file.write(f'({edge[0]}, {edge[1]}, {edge[2]})\n')
