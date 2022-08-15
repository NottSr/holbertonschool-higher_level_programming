#!/usr/bin/node

/* Script that prints My number: <first argument converted in integer> */

const args = process.argv;
const Num = parseInt(args[2]);

if (isNaN(Num) === false) {
  console.log('My number: ' + Num);
} else {
  console.log('Not a number');
}
