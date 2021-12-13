#!/usr/bin/node
const n = parseInt(process.argv[2]);
console.log(factorial(n));

function factorial (n) {
  if (n === 1 || Number.isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
