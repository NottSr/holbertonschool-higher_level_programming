#!/usr/bin/node

/* Script that prints the number of movies where the character “Wedge Antilles” is present */

const arg = process.argv[2];
const axios = require('axios').default;

axios.get('https://swapi-api.hbtn.io/api/films/' + arg)
  .then(function (response) {
    // Success execution
    for (const key of response.data.characters) {
      axios.get(key)
        .then((res) => {
          console.log(res.data.name);
        });
    }
  });
