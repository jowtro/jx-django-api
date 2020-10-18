#!/bin/bash
#if fails at any point break the script
set -e
 
#read vars from file
env_file=".env.dev"
source .env.dev
# export all vars from file
export $(cut -d= -f1 $env_file)
echo "##############################################"
echo "#     START POSTGRES CONTAINER FIRST!        #"
echo "##############################################"
echo "##############################################"
echo "  It's supposed to run with venv activated!"
echo "##############################################"

echo "Running python App ..."
cd app && python manage.py runserver 0.0.0.0:8000