#!/usr/bin/node

/* Script that prints all characters of a Star Wars movie */

const arg = process.argv[2];
const axios = require('axios').default;

axios.get('https://swapi-api.hbtn.io/api/films/' + arg)
  .then(function (response) {
    // Success execution
    for (const key of response.data.characters) {
      async function pChar() {
        try {
          const res = await axios.get(key);
          console.log(res.data.name);
        } catch (error) {
          console.error(error);
        }
      };
      pChar();
    }
  });
