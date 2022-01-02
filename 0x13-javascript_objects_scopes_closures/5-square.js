#!/usr/bin/node
// class square that inherits from class rectangle
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};