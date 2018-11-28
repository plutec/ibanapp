#!/usr/bin/env bash

apt-get update
apt-get install -y python3-pip
apt-get install -y apache2
pip install -r /vagrant/requirements.txt
#if ! [ -L /var/www ]; then
#  rm -rf /var/www
#  ln -fs /vagrant /var/www
#fi



