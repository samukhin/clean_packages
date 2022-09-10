import subprocess

#Получаем список всех пакетов и зависимостей
deps = subprocess.check_output("apt-cache depends --installed --no-recommends --no-suggests --no-conflicts --no-breaks --no-replaces --no-enhances $(apt list --installed 2>/dev/null | awk -F '/' 'NR>1{print $1}')", shell=True).decode("utf-8").split('\n')

#Создаём переменные
d = {}
key = ''

#Заполняем словарь пустотой
for dep in deps:
    if dep == '':
        continue
    if dep[0] != ' ':
        d[dep] = []

#Заполняем словарь пакетами и зависимостями
for dep in deps:
    if dep == '':
        continue
    if dep[0] != ' ':
        key = dep
    else:
        cdep = dep.split(' ')[-1]
        if cdep in d:
            if not cdep in d[key]:
                d[key] += [cdep]

#Начинаем действия с networkx
import networkx as nx
G = nx.DiGraph()

G.clear()

for package in d.keys():
    for dep in d[package]:
        G.add_edge(package, dep)

print([len(i) for i in nx.connected_components(G.to_undirected())])

comp_list = list(nx.connected_components(G.to_undirected()))


def print_dep(package, dep_level):
    global G
    global blist
    blist += [package]
    if len(G.adj[package]) > 0:
        for i in G.adj[package]:
            print(' '*dep_level+i)
            if not i in blist:
                print_dep(i, dep_level+1)
            if dep_level == 1:
                blist = []


blist = []
for package in G.nodes():
    if len(G.pred[package]) == 0:
        for i in range(len(comp_list)):
            if package in comp_list[i]:
                print(package, i)
                break
        print_dep(package, 1)
        blist = []
