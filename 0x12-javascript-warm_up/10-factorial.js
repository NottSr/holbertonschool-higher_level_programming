#!/usr/bin/node

/* Script that computes and prints a factorial */

const args = process.argv;
const x = parseInt(args[2]);

console.log(factorial(x));

function factorial (a) {
  if (isNaN(a)) {
    return (1);
  }

  if (a < 0) {
    return (-1);
  } else if (a === 0) {
    return (1);
  } else {
    return (a * factorial(a - 1));
  }
}
