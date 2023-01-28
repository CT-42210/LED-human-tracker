#BASH

sudo apt update && sudo apt upgrade -y && sudo apt autoremove

echo 'interface eth0' /etc/dhcpcd.conf
echo 'nogateway' /etc/dhcpcd.conf

cd Desktop || exit
git clone https://github.com/CT-42210/LED-human-tracker

cd LED-human-tracker || exit
mv git-pull.sh /home/pi
