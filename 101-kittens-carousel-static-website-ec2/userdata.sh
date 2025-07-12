#!/bin/bash -x

dnf update -y
dnf install httpd -y

cd /var/www/html