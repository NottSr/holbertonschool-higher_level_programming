#!/usr/bin/node

/* Script that prints x times “C is fun” */

const args = process.argv;
const x = parseInt(args[2]);
let i = 0;

if (isNaN(x)) {
  console.log('Missing number of occurrences');
}

while (i < x) {
  console.log('C is fun');
  i++;
}
