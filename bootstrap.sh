#!/usr/bin/env bash

apt-get update
apt-get install -y python3-pip
apt-get install -y apache2
pip3 install --upgrade pip
pip3 install -r /vagrant/requirements.txt

cd /vagrant/ibanapp
python3 manage.py migrate
#python3 manage.py runserver 0.0.0.0:8000
#if ! [ -L /var/www ]; then
#  rm -rf /var/www
#  ln -fs /vagrant /var/www
#fi



