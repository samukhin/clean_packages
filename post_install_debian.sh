*#Debian 9-11

apt purge --autoremove (локальные пакеты)
apt purge --autoremove linux-image-(старые)

apt purge --autoremove gcc-(старый) installation-report

apt purge --autoremove xterm*
apt purge --autoremove libreoffice*
apt purge --autoremove avahi* libavahi
apt purge --autoremove packagekit*
apt purge --autoremove gnome-keyring*
apt purge --autoremove apparmor*
apt purge --autoremove rsyslog*
apt purge --autoremove cron anacron

#Так как alsa практически нигде не используется
apt purge alsa*
#либо так, но от pulse много чего зависит
apt purge pulseaudio*

#Debian 11
apt purge --autoremove pipewire*
apt purge --autoremove libpipewire*
