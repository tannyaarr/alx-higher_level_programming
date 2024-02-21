#!/usr/bin/node
const request = require('request'); const url = process.argv[2]; const filePath = process.argv[3]; const fs = require('fs');

if (!url || !filePath) console.log('Usage: ./get_webpage.js <url> <file_path>');
else request(url, (error, response, body) => fs.writeFileSync(filePath, body, 'utf-8'));
