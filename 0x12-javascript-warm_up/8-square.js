#!/usr/bin/node

/* Script that prints a square */

const args = process.argv.map(item => item[0]).filter(val => !isNaN(val));
const x = parseInt(args[0]);
let i = 0;

if (isNaN(x)) {
  console.log('Missing size');
} else {
  while (i < x) {
    console.log('X'.repeat(x));
    i++;
  }
}
