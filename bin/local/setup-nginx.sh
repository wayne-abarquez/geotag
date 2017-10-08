#!/usr/bin/env bash

# TODO: Change project dir name

sudo rm /etc/nginx/sites-enabled/default
sudo rm /etc/nginx/sites-available/demo_boilerplate
sudo rm /etc/nginx/sites-enabled/demo_boilerplate
sudo cp conf/local/nginx.conf /etc/nginx/sites-available/demo_boilerplate
sudo ln -s /etc/nginx/sites-available/demo_boilerplate /etc/nginx/sites-enabled/demo_boilerplate
sudo /etc/init.d/nginx reload
