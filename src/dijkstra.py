import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    # Inisialisasi jarak dari simpul awal ke semua simpul lainnya sebagai tak terhingga
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Inisialisasi semua jalur sebagai jalur kosong
    paths = {node: [] for node in graph}
    # Jalur dari simpul awal ke dirinya sendiri hanya berisi simpul awal
    paths[start] = [start]

    # Daftar simpul yang harus dikunjungi
    nodes_to_visit = list(graph.keys())

    while nodes_to_visit:
        # Pilih simpul dengan jarak terkecil dari simpul awal
        current_node = min(nodes_to_visit, key=lambda node: distances[node])
        # Hapus simpul tersebut dari daftar simpul yang harus dikunjungi
        nodes_to_visit.remove(current_node)

        for neighbor, weight in graph[current_node].items():
            # Hitung jarak melalui simpul saat ini ke tetangga
            distance = distances[current_node] + weight
            # Jika jarak ini lebih kecil dari jarak terpendek yang ditemukan sejauh ini
            if distance < distances[neighbor]:
                # Perbarui jarak terpendek
                distances[neighbor] = distance
                paths[neighbor] = paths[current_node] + [neighbor]
    return distances, paths

def draw_graph(graph, path):
    # Membuat objek graf kosong
    G = nx.Graph()

    # Menambahkan setiap tepi dan bobotnya ke graf
    for node, edges in graph.items():
        for edge, weight in edges.items():
            G.add_edge(node, edge, weight=weight)

    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Membuat graf berarah untuk jalur terpendek
    H = nx.DiGraph()
    path_edges = [(path[i], path[i+1]) for i in range(len(path) - 1)]
    H.add_edges_from(path_edges)
    nx.draw_networkx_edges(H, pos, edgelist=path_edges, edge_color='r', width=2, arrowstyle='-|>', arrowsize=20)

    plt.show()