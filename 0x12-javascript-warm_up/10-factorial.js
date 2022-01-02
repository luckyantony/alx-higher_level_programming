#!/usr/bin/node
// Computes and prints a factorial
function factorial (factor) {
  if (factor === 0) {
    return 0;
  } else if (factor === 1) {
    return 1;
  } else {
    return (factor * factorial(factor -1));
  }
}
const myVar = parseInt(process.argv[2]);
if (isNaN(myVar) || myVar === undefined) {
  console.log('1');
} else {
  console.log(factorial(myVar));
}