#!/bin/bash
# Script that sends a GET request to the URl
url="$1"
curl_output=$(curl -s -w "%{http_code}" "$1")
[ "$(tail -c 4 <<< "$curl_output")" == "200" ] && echo "$(sed '$d' <<< "$curl_output")"
