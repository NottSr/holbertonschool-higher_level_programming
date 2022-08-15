#!/usr/bin/node

/* Script that prints the addition of 2 integers */

const args = process.argv;
const x = parseInt(args[2]);
const y = parseInt(args[3]);

console.log(add(x, y));

function add (a, b) {
  return (a + b);
}
