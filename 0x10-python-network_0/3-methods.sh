#!/bin/bash
# Dislays all HTTP methods the server will accept
curl -I -X OPTIONS "$1" | grep "Allow" | cut -d " " -f 2-
