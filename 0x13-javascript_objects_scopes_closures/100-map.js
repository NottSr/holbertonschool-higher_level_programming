#!/usr/bin/node

/* Script that imports an array and computes a new array */

const list = require('./100-data.js').list;
const map1 = list.map((x, index) => x * index);

console.log(list);
console.log(map1);
