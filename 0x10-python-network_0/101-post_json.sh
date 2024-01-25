#!/bin/bash
# SEnds a JSON POST request to a URL
curl -s -H "Content-Type: application/json" -d "@$2" -X POST "$1"
