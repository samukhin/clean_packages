print("Start")
print("Library importing")
import subprocess


print("Getting packages")
#Получаем список всех пакетов
packages = subprocess.check_output("apt list --installed 2>/dev/null | awk -F '/' 'NR>1{print $1}'", shell=True).decode("utf-8").split('\n')


print("Creating dict")
#Создаём словарь всех пакетов
info = {}
#Создаём словарь для всех зависимостей
ddeps = {}


print("Creating subdict")
#В цикле по всем пакетам
for pn in packages[0:]:
    #Если пакет не пустой
    if pn != '':
        #Создаём подсловарь
        info[pn] = {}
        #Получаем список всех зависимостей
        deps = subprocess.check_output("apt-cache depends --installed " + pn, shell=True).decode("utf-8").split('\n')
        #Кладём зависимости в словарь зависимостей
        ddeps[pn] = deps


print("Creating sumarray")
#В цикле по всем пакетам
for pn in info.keys():
    #Получаем список всех зависимостей
    deps = ddeps[pn]
    #Идём по всем зависимостям (0 элемент - сам родитель)
    for dep in deps[1:]:
        #Если зависимость не пуста
        if dep != '':
            #Парсим [тип_зависимости, зависимость]
            pdep = dep.split(' ')[-2:]
            #Создаём массив для типов зависимостей
            if pdep[0] != '':
                info[pn][pdep[0]] = []
                #Создаём массивы для обратных зависимостей
                info[pdep[1]]['-'+pdep[0]] = []


print("Polling subdict and sumarray")
#В цикле по всем ключам словаря
for pn in info.keys():
    #Получаем список всех зависимостей
    deps = ddeps[pn]
    #Идём по всем зависимостям (0 элемент - сам родитель)
    for dep in deps[1:]:
        #Если зависимость не пуста
        if dep != '':
            #Парсим [тип_зависимости, зависимость]
            pdep = dep.split(' ')[-2:]
            #Создаём массив для типов зависимостей
            if pdep[0] != '':
                info[pn][pdep[0]] += [pdep[1]]
                #Заполнение обратных зависимостей
                info[pdep[1]]['-'+pdep[0]] += [pn]


print("Printing packages")
#В цикле по всем ключам словаря
for pn in info.keys():
    #Если не нашлось обратный зависимостей
    if not '-' in ''.join(info[pn].keys()):
        #Выводим  пакет на экран
        print(pn)
