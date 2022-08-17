#!/usr/bin/node

/* Script that prints the title of a Star Wars movie where the episode number matches a given integer */

const axios = require('axios').default;

axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2])
  .then(function (response) {
    // Success execution
    console.log(response.data.title);
  })
  .catch(function (err) {
    // Error execution
    console.log('code: ' + err.response.status);
  });
