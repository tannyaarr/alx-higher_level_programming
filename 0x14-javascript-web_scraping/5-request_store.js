#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];
const fs = require('fs');

request(url).pipe(fs.createWriteStream(filePath));
