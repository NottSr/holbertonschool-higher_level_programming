#!/usr/bin/node

/* Script that imports a dictionary of occurrences by user id
and computes a dictionary of user ids by occurrence */

const dict = require('./101-data.js').dict;
const nDict = {};

Object.keys(dict).map(key => {
  if (!Array.isArray(nDict[dict[key]])) {
    nDict[dict[key]] = [];
  }
  nDict[dict[key]].push(key);
});

console.log(nDict);
