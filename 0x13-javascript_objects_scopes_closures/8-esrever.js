#!/usr/bin/node
exports.esrever = function (list) {
  if (!Array.isArray(list)) {
    throw new Error('Input is not an array');
  }
  const reversedList = [...list];
  for (let i = 0, j = reversedList.length - 1; i < j; i++, j--) {
    const temp = reversedList[i];
    reversedList[i] = reversedList[j];
    reversedList[j] = temp;
  }
  return reversedList;
};
