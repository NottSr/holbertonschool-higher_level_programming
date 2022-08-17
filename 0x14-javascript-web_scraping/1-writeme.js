#!/usr/bin/node

/* Script that writes content to a file */

const args = process.argv;
const fs = require('fs');

fs.writeFile(args[2], args[3], (err) => {
  if (err) {
    console.error(err);
  }
});
