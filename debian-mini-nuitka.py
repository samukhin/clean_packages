import subprocess

#Получаем список всех пакетов и зависимостей
deps = subprocess.check_output("apt-cache depends --installed --no-recommends --no-suggests --no-conflicts --no-breaks --no-replaces --no-enhances $(dpkg-query -W --showformat='${Package} ')", shell=True).decode("utf-8").split('\n')

#Создаём переменные
d = {}
key = ''

#Заполняем словарь пустотой
for dep in deps:
    if dep == '':
        continue
    if dep[0] != ' ':
        d[dep] = {}
        d[dep]["dep"] = []
        d[dep]["rdep"] = []

#Заполняем словарь пакетами и зависимостями
for dep in deps:
    if dep == '':
        continue
    if dep[0] != ' ':
        key = dep
    else:
        cdep = dep.split(' ')[-1]
        if cdep in d:
            if not cdep in d[key]["dep"]:
                d[key]["dep"] += [cdep]
            if not key in d[cdep]["rdep"]:
                d[cdep]["rdep"] += [cdep]

#Функция вывода зависимостей из словаря
def print_dep(package, dep_level):
    global d
    global blist
    blist += [package]
    if len(d[package]["dep"]) > 0:
        for dep in d[package]["dep"]:
            print(' ' * dep_level + dep)
            if not dep in blist:
                print_dep(dep, dep_level+1)
            if dep_level == 1:
                blist = []

#Выводим иерархию пакетов
blist = []
for package in d.keys():
    if len(d[package]["rdep"]) == 0:
        print_dep(package, 0)
        blist = []
