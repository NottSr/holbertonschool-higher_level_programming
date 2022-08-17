#!/usr/bin/node

/* Function that returns the reversed version of a list */

exports.esrever = function (list) {
  return list.sort((a, b) => { return b - a; });
};
