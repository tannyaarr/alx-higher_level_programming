#!/bin/bash
# Script that sends a DELETE request to the url passed as the first argument

curl -X DELETE -s $1
