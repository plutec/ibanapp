#!/usr/bin/env bash

#General configuration
apt-get update
apt-get install -y python3-pip
apt-get install -y apache2
pip3 install --upgrade pip
pip3 install pipenv

# PostgreSQL
apt-get install -y python3-dev libpq-dev postgresql postgresql-contrib
