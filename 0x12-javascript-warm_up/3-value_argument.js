#!/usr/bin/node
// Prints first argument passed to a script
const myVar = process.argv[2];
if (myVar === undefined) {
  console.log('No argument');
} else {
  console.log(myVar);
}