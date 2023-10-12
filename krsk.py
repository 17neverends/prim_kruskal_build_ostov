import matplotlib.pyplot as plt
import networkx as nx

massiv = []

while True:
    try:
        values = input("Введите три значения (через пробел): ")
        if not values:
            break
        values = list(map(int, values.split()))
        massiv.append(values)
    except ValueError:
        print("Неправильный формат данных. Пожалуйста, введите три целых числа.")

massivsorted = sorted(massiv, key=lambda x: x[0])
connected = set()
D = {}
T = []


def st1():
    for v in massivsorted:
        if v[1] not in connected or v[2] not in connected:
            if v[1] not in connected and v[2] not in connected:
                D[v[1]] = [v[1], v[2]]
                D[v[2]] = D[v[1]]
            else:
                if not D.get(v[1]):
                    D[v[2]].append(v[1])
                    D[v[1]] = D[v[2]]
                else:
                    D[v[1]].append(v[2])
                    D[v[2]] = D[v[1]]
            T.append(v)
            connected.add(v[1])
            connected.add(v[2])
    return T


def st2():
    for v in massivsorted:
        if v[2] not in D[v[1]]:
            T.append(v)
            gv1 = D[v[1]]
            D[v[1]] += D[v[2]]
            D[v[2]] += gv1
    return T


st1()
st2()
a = st2()
c = []
for i in a:
    b = i[-2:]
    b.append(i[0])
    c.append(b)
FG = nx.Graph()
FG.add_weighted_edges_from(c)
elarge = [(u, v) for (u, v, d) in FG.edges(data=True) if d["weight"] != c[0][2]]
esmall = [(u, v) for (u, v, d) in FG.edges(data=True) if d["weight"] == c[0][2]]
pos = nx.spring_layout(FG, seed=7)
nx.draw_networkx_nodes(FG, pos, node_size=700)
nx.draw_networkx_edges(FG, pos, edgelist=elarge, width=6)
nx.draw_networkx_edges(
    FG, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed")
nx.draw_networkx_labels(FG, pos, font_size=20, font_family="sans-serif")
edge_labels = nx.get_edge_attributes(FG, "weight")
nx.draw_networkx_edge_labels(FG, pos, edge_labels)
ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()
