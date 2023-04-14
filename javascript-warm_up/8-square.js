#!/usr/bin/node

const printSize = parseInt(process.argv[2]);

if (isNaN(printSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < printSize; i++) {
    let row = '';
    for (let j = 0; j < printSize; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
