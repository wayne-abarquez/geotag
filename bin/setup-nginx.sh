#!/usr/bin/env bash

# TODO: Change project dir name

sudo rm /etc/nginx/sites-enabled/default
sudo rm /etc/nginx/sites-available/geotag
sudo rm /etc/nginx/sites-enabled/geotag
sudo cp conf/nginx.conf /etc/nginx/sites-available/geotag
sudo ln -s /etc/nginx/sites-available/geotag /etc/nginx/sites-enabled/geotag
sudo /etc/init.d/nginx reload
