#!/bin/bash
# Sends a POST request to the passed url

curl -X POST -H "Content-Type: application/json" -d '{"email":"test@gmail.com","subject":"I will always be here for PLD"}' $1
