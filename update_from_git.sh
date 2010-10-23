#! /bin/bash


#pulls the latest source from github.
#Restarts apache
#should be run as root
#by akittredge October 2010

stop mysql
git pull
start mysql
