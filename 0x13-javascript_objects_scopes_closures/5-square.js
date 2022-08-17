#!/usr/bin/node

/* Class Square that defines a square inherits Rectangle */

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
