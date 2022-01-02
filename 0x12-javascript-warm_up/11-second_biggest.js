#!/usr/bin/node
// Searches second boggest integer in the list of arguments
if (process.argv.length === 1) {
  console.log('0');
} else {
  const value = process.argv.slice(2).map(x => parseInt(x));
  value.sort(function (a, b) { return b - a; });
  console.log(value[1]);
}