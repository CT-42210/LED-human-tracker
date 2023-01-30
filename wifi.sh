# bash
echo -e "WARNING: This script is one time use, do not run twice.\nThis will restart the Pi."
read -p "Are you sure? [Y/n]" -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
  #fix ethernet problem
  echo 'interface eth0' >> /etc/dhcpcd.conf
  echo '  nogateway' >> /etc/dhcpcd.conf

  sudo reboot
fi
