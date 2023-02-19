#!/bin/bash
# This runs on the production server: fetches new code,
# Installs needed packages, and restarts the server.

echo "Pulling code from master"
git pull origin master

echo "Installing packages"
pip install -r requirements.txt

echo "Going to reboot the webserver"
touch /var/www/kip218_pythonanywhere_com_wsgi.py

echo "Finished rebuild."