#!/usr/bin/node
let msg = process.argv[2];
if (msg === undefined) {
  msg = 'No argument';
}
console.log(msg);
