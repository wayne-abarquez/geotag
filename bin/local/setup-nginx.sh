#!/usr/bin/env bash

sudo rm /etc/nginx/sites-enabled/default
sudo rm /etc/nginx/sites-available/geotag
sudo rm /etc/nginx/sites-enabled/geotag
sudo cp conf/local/nginx.conf /etc/nginx/sites-available/geotag
sudo ln -s /etc/nginx/sites-available/geotag /etc/nginx/sites-enabled/geotag
sudo /etc/init.d/nginx reload
