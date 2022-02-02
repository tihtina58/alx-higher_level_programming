#!/usr/bin/node

const URL = process.argv[2];
const request = require('request');
request
  .get(URL)
  .on('response', function (response) {
    console.log('code:', response.statusCode);
  });
