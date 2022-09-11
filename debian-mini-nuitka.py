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

#Выводим пакеты без родителей
for package in d:
    if len(d[package]["rdep"]) == 0:
        print(package)
