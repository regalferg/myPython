#!/bin/bash
if [ -f "/tmp/labrunning" ] ; then
  echo "                                       "
  echo -e "\033[0;31m        ▄██████████████▄▐█▄▄▄▄█▌       \033[0m" 
  echo -e "\033[0;31m        ██████▌▄▌▄▐▐▌███▌▀▀██▀▀        \033[0m" 
  echo -e "\033[0;31m        ████▄█▌▄▌▄▐▐▌▀███▄▄█▌          \033[0m" 
  echo -e "\033[0;31m        ▄▄▄▄▄██████████████▀           \033[0m" 
  echo "                                       "
  echo " --> ! You forgot to teardown.sh ! <-- "
  echo "                                       "
  echo " Take 10s to think about what you did. "
  secs=$((10))
  while [ $secs -gt 0 ]; do
    echo -ne "                   $secs\033[0K\r"
    sleep 1
    : $((secs--))
  done
  echo " Lab setup failed! You know what to do."
  exit 1
else
  touch /tmp/labrunning
fi
echo "Building lab..."

### Create networks
sudo docker network create --opt com.docker.network.driver.mtu=1450 --subnet 10.10.2.0/24 ansible-net

sudo docker build -q --build-arg user=bender     --tag ssh-bender     $HOME/.config/dockerfiles/ansible/ssh-ks
sudo docker build -q --build-arg user=fry        --tag ssh-fry        $HOME/.config/dockerfiles/ansible/ssh-ks
sudo docker build -q --build-arg user=zoidberg   --tag ssh-zoidberg   $HOME/.config/dockerfiles/ansible/ssh-ks
sudo docker build -q --build-arg user=farnsworth --tag ssh-farnsworth $HOME/.config/dockerfiles/ansible/ssh-centos

### Launch containers and connect networks
sudo docker run -d  --name bender      -h bender     --ip 10.10.2.3 --network ansible-net ssh-bender
sudo docker run -d  --name fry         -h fry        --ip 10.10.2.4 --network ansible-net ssh-fry
sudo docker run -d  --name zoidberg    -h zoidberg   --ip 10.10.2.5 --network ansible-net ssh-zoidberg
sudo docker run -d  --name farnsworth  -h farnsworth --ip 10.10.2.6 --network ansible-net ssh-farnsworth

echo "Complete!"
