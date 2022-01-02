#!/usr/bin/node
// prints messages depending on the number of arguments passed
const myVar = process.argv.length;
if (myVar === 2) {
  console.log('No argument');
} else if (myVar === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}