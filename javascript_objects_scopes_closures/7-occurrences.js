#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const filteredList = list.filter(el => el === searchElement);
  return filteredList.length;
};
