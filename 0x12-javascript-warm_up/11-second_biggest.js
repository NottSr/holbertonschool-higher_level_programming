#!/usr/bin/node

/* Script that searches the second biggest integer in the list of arguments. */

const args = process.argv;
let i = 4;
let sbig = 0;
let big = 0;

if (args[3]) {
  if (args[2] > args[3]) {
    big = parseInt(args[2]);
    sbig = parseInt(args[3]);
  } else {
    big = parseInt(args[3]);
    sbig = parseInt(args[2]);
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
