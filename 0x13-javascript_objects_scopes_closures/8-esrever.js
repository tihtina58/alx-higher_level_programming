#!/usr/bin/node

exports.esrever = function (list) {
  const rev = [];
  const len = list.length;

  for (let i = 0; i < len; i++) {
    rev.push(list[len - 1 - i]);
  }

  return (rev);
};
