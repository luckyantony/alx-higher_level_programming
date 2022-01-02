#!/usr/bin/node
// Prints a square
const Size = parseInt(process.argv[2]);
if (isNaN(Size) || Size === undefined) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < Size) {
    console.log(`${Array(Size).fill('X').join('')}`);
    i++;
  }
}