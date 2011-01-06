#! /bin/bash


#pulls the latest source from github.
#Restarts apache
#should be run as root
#by akittredge October 2010
rm -f *.pyc
git pull
mysql -u root -pand376sc foreclosed < foreclosed.sql
cp static/* /var/www/
/etc/init.d/apache2 restart
