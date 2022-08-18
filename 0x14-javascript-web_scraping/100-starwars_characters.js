#!/usr/bin/node

/* Script that prints all characters of a Star Wars movie */

const axios = require('axios').default;

axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2])
  .then(function (response) {
    // Success execution
    for (const key of response.data.characters) {
      axios.get(key)
        .then((res) => {
          console.log(res.data.name);
        });
    }
  });
