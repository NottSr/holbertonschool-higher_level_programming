#!/usr/bin/node

/* Script that searches the second biggest integer in the list of arguments. */

let arr = process.argv.slice(2);

if (arr.length < 2) {
  console.log(0);
} else {
  arr = arr.map(Number);
  arr = [...new Set(arr)];
  arr = arr.sort((a, b) => { return b - a; });
  console.log(arr[1]);
}
