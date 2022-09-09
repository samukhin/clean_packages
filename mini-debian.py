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
            d[key] += [cdep]
