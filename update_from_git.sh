#! /bin/bash


#pulls the latest source from github.
#Restarts apache
#should be run as root
#by akittredge October 2010

git pull
mysql -u root -pand376sc foreclosed < foreclosed.sql
