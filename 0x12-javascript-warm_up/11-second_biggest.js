#!/usr/bin/node

/* Script that searches the second biggest integer in the list of arguments. */

const args = process.argv.map(item => item[0]).filter(val => !isNaN(val));
let i = 2;
let s_big = 0;
let big = 0;

if (args[1]) {
  if (args[0] > args[1]) {
    big = parseInt(args[0]);
    s_big = parseInt(args[1]);
  } else {
    big = parseInt(args[1]);
    s_big = parseInt(args[0]);
  }

  while (i < args.length) {
    if (args[i] > big) {
      s_big = big;
      big = args[i];
    } else if (args[i] > s_big) {
      s_big = args[i];
    }
    i++;
  }

  console.log(s_big);
} else {
  console.log('0');
}
