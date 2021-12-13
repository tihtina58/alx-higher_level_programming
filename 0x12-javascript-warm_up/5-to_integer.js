#!/usr/bin/node
const integer = process.argv[2];
let message = '';
if (integer === undefined) {
  message = 'Not a number';
} else {
  if (Number.isNaN(parseInt(integer))) {
    message = 'Not a number';
  } else {
    message = 'My number: ' + parseInt(integer);
  }
}
console.log(message);
