#! /bin/bash


#pulls the latest source from github.
#Restarts apache
#should be run as root
#by akittredge October 2010
rm *.pyc
git pull
mysql -u root -pand376sc foreclosed < foreclosed.sql
/etc/init.d/apache2 restart
