#BASH
echo -e "WARNING: This script is one time use, do not run twice. \nThis will restart the Pi."
read -p "Are you sure? [Y/n]" -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
  #sudo apt update && sudo apt upgrade -y && sudo apt autoremove
#
  #echo 'interface eth0' /etc/dhcpcd.conf
  #echo 'nogateway' /etc/dhcpcd.conf
#
  #cd Desktop || exit
  #git clone https://github.com/CT-42210/LED-human-tracker
#
  #cd LED-human-tracker || exit
  #git config pull.rebase false
  #mv git-pull.sh /home/pi

  cd || exit

  git clone https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi.git
  mv TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi tflite1

  sudo apt -y install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
  sudo apt -y install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
  sudo apt -y install libxvidcore-dev libx264-dev
  sudo apt -y install qt4-dev-tools
  sudo apt -y install libatlas-base-dev

  pip install opencv-python==3.4.11.41
  pip install https://github.com/google-coral/pycoral/releases/download/v2.0.0/tflite_runtime-2.5.0.post1-cp39-cp39-linux_armv7l.whl

  wget https://storage.googleapis.com/download.tensorflow.org/models/tflite/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip
  unzip coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip -d Sample_TFLite_model

  sudo reboot
fi
