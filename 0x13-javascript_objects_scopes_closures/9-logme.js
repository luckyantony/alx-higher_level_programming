#!/usr/bin/node
// prints the number of arguments already printed and the new argument value
let count = 0;
exports.logme = function (item) {
  console.log(count + ': ' + item);
  count++;
};