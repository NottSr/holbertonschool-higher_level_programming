#!/usr/bin/node

/* Script that computes the number of tasks completed by user id */

const args = process.argv;
const axios = require('axios').default;
const dict = {};

axios.get(args[2])
  .then(function (response) {
    for (const elem of response.data) {
      if (elem.completed === true) {
        if (dict[elem.userId] === undefined) {
          dict[elem.userId] = 1;
        } else {
          dict[elem.userId] += 1;
        }
      }
    }
    console.log(dict);
  });
