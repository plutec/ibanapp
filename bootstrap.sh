#!/usr/bin/env bash

#General configuration
apt-get update
apt-get install -y python3-pip python3-dev
pip3 install --upgrade pip
sudo pip3 install pipenv

# PostgreSQL
apt-get install -y libpq-dev postgresql postgresql-contrib tox

