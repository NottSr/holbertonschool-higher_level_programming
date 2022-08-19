#!/usr/bin/node

/* Script that imports a dictionary of occurrences by user id
and computes a dictionary of user ids by occurrence */

const dict = require('./101-data.js').dict;
const nDict = {};

for (const key in dict) {
  if (!nDict[dict[key]]) {
    nDict[dict[key]] = [];
  }
  nDict[dict[key]].push(key);
}

console.log(nDict);
