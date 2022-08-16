#!/usr/bin/node

/* Class Rectangle that defines a rectangle */

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w && w > 0) && (h && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
