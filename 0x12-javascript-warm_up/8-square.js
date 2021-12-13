#!/usr/bin/node
const arg = process.argv[2];
const num = parseInt(arg);
let line = '';

if (Number.isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    line += 'X';
  }
  for (let i = 0; i < num; i++) {
    console.log(line);
  }
}
