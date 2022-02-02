#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const wedge = 'https://swapi-api.hbtn.io/api/people/18/';
request(url, function (error, response, body) {
  let counter = 0;
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    for (let i = 0; i < results.length; i++) {
      if (results[i].characters.includes(wedge) === true) {
        counter += 1;
      }
    }
  }
  console.log(counter);
});
