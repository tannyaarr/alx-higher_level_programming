#!/usr/bin/node
const fs = require('fs');

filePath = process.argv[2];
contentToWrite = process.argv[3];

if (!filePath || !contentToWrite);
else fs.writeFile(filePath, contentToWrite, 'utf-8', (err) => console.log(err));
