#!/bin/bash
# Script that sends a DELETE request to the url passed as the first argument
curl -s -X DELETE "$1"
