#!/usr/bin/node
// function converts a number from base 10 to another base passed as argument
exports.converter = function (base) {
    return function (nbase) {
      return (nbase.toString(base));
    };
  };