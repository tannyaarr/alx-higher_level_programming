#!/bin/bash
# Use curl to make a request that causes the server to respond with "You got me!"
curl -X PUT -L --data "user_id=98" --header "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
