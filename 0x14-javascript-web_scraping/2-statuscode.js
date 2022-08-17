#!/usr/bin/node

/* Script that display the status code of a GET request */

const axios = require('axios').default;

axios.get(process.argv[2])
  .then(function (response) {
    // Success execution
    console.log('code: ' + response.status);
  })
  .catch(function (error) {
    // Error execution
    console.error('code: ' + error.response.status);
  });
