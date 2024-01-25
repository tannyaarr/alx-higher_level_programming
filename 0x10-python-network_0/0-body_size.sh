#!/bin/bash
# Script that displays the size of the body reponse
curl -sI "$1" | grep -i content-length | awk '{print $2}' | tr -d '\r'
