#!/usr/bin/node

/* Script that reads and prints the content of a file */

const args = process.argv;
const fs = require('fs');

fs.readFile(args[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
