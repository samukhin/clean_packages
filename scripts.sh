apt-cache depends --recurse --no-recommends --no-suggests --no-conflicts --no-breaks --no-replaces --no-enhances <your-package-here> | grep "^\w" | sort -u


dpkg-query -W --showformat='${Package}\t${Priority}\n'

dpkg-query -W --showformat='${Package}\t${Depends}\n'

#Отметить все пакеты как установленные автоматически
aptitude markauto $(dpkg-query -W --showformat='${Package} ')
apt-mark markauto $(dpkg-query -W --showformat='${Package} ')
apt-mark auto $(apt-mark showmanual)

dpkg -l | grep '^rc' | awk '{print $2}' | xargs dpkg --purge

apt-cache depends --installed --no-recommends --no-suggests --no-conflicts --no-breaks --no-replaces --no-enhances $(apt list --installed 2>/dev/null | awk -F '/' 'NR>1{print $1}') > list
