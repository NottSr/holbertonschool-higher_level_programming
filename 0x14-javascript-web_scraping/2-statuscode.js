#!/usr/bin/node

/* Script that display the status code of a GET request. */

const axios = require('axios').default;

axios.get(process.argv[2])
  .then(function (response) {
    // handle success
    console.log('code: ' + response.status);
  })
  .catch(function (error) {
    // handle error
    console.log('code: ' + error.response.status);
  });
