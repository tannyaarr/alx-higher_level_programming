#!/usr/bin/node
exports.converter = function (base) {
  function convertRecursive (number) {
    if (number === 0) {
      return '';
    }
    const remainder = number % base;
    const quotient = Math.floor(number / base);
    return convertRecursive(quotient) + remainder;
  }
  return function (number) {
    return number === 0 ? '0' : convertRecursive(number);
  };
};
