#!/bin/bash
# Script that sends a GET request to the URL
response=$(curl -s -o /dev/null -w "%{http_code}" $1)
if [ $response -eq 200 ]
then
    curl -s $1
else
    echo "Error: Response code $response"
fi
