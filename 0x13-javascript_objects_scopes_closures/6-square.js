#!/usr/bin/node

const SquareParent = require('./5-square');

class Square extends SquareParent {
  charPrint (c) {
    let charac = c;
    let str = '';

    if (charac === undefined) {
      charac = 'X';
    }

    for (let j = 0; j < this.width; j++) {
      str += charac;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(str);
    }
  }
}
module.exports = Square;
