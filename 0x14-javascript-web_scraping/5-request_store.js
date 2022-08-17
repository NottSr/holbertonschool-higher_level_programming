#!/usr/bin/node

/* Script that gets the contents of a webpage and stores it in a file */

const args = process.argv;
const fs = require('fs');
const axios = require('axios').default;

axios.get(args[2])
  .then(function (response) {
    fs.writeFile(args[3], response.data, (err) => {
      if (err) {
        console.error(err);
      }
    });
  });
