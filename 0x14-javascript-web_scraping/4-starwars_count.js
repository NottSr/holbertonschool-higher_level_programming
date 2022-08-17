#!/usr/bin/node

/* Script that prints the number of movies where the character “Wedge Antilles” is present */

const arg = process.argv[2];
const axios = require('axios').default;

axios.get(arg)
  .then(function (response) {
    // Success execution
    let count = 0;
    for (const key of response.data.results) {
      for (const elem of key.characters) {
        if (elem.endsWith('18/')) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  });
