#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const words = process.argv[3];

// fs.writeFileSync(ファイルのパス, 書き込む文字, 文字コード, コールバック関数)
fs.writeFileSync(filePath, words, 'utf-8', (err) => {
  if (err) {
    console.log(err);
    process.exit(1);
  }
});
