#!/usr/bin/node

/* Script that prints the title of a Star Wars movie where the episode number matches a given integer */

const args = process.argv;
const fs = require('fs');
const axios = require('axios').default;

axios.get(args[2])
  .then(function (response) {
    fs.writeFile(args[3], response.data, (err) => {
      if (err) {
        console.error(err);
      }
    })
  });
