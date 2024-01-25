#!/bin/bash
# Script that sends a GET request and disply only body of a 200 status code
curl -s -X GET "$1"
