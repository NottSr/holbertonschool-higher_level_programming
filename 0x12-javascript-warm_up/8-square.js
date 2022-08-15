#!/usr/bin/node

/* Script that prints a square */

const args = process.argv;
const x = parseInt(args[2]);
let i = 0;

if (isNaN(x)) {
  console.log('Missing size');
}

while (i < x) {
  console.log('X'.repeat(x));
  i++;
}
