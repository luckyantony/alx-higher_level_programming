#!/usr/bin/node
// Returns number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
    let count = 0;
    for (const i of list) {
      if (i === searchElement) {
        count++;
      }
    }
    return count;
  };