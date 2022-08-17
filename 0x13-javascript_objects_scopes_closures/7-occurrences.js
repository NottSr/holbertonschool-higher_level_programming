#!/usr/bin/node

/* Function that returns the number of occurrences in a list */

exports.nbOccurences = function (list, searchElement) {
  let nbo = 0;

  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      nbo += 1;
    }
  }

  return (nbo);
};
