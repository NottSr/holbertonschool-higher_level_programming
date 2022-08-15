#!/usr/bin/node

/* Script that searches the second biggest integer in the list of arguments. */

const args = process.argv.map(item => item[0]).filter(val => !isNaN(val));
let i = 2;
let sbig = 0;
let big = 0;

if (args[1]) {
  if (args[0] > args[1]) {
    big = parseInt(args[0]);
    sbig = parseInt(args[1]);
  } else {
    big = parseInt(args[1]);
    sbig = parseInt(args[0]);
  }

  while (i < args.length) {
    if (args[i] > big) {
      sbig = big;
      big = args[i];
    } else if (args[i] > sbig) {
      sbig = args[i];
    }
    i++;
  }

  console.log(sbig);
} else {
  console.log('0');
}
