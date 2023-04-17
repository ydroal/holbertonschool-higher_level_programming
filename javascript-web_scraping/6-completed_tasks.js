#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const res = {};

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const obj = JSON.parse(body);
  for (let i = 1; i <= 10; i++) {
    const filteredList = obj.filter(e => e.userId === parseInt(i)).filter(id => id.completed === true);
    res[parseInt(i)] = filteredList.length;
  }
  Object.keys(res).forEach(key => {
    if (res[key] === 0) {
      delete res[key];
    }
  });
  console.log(res);
});
