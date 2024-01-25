#!/bin/bash
# Script that takes in a url and sends a request and displays the size of the body reponse

response=$(curl -s -o /dev/null -w "%{size_download}" $1)
echo "The size of the reponse body is $reponse bytes."
