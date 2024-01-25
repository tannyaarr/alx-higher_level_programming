#!/bin/bash
# Script that takes in a url amd sends a request and displays the size of the body reponse

url="$1"
curl -sI "$1" | grep -i content-length | awk '{print $2}' | tr -d '\r'
