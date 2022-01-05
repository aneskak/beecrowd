var input = require("fs").readFileSync("stdin", "utf8");

var pi = 3.14159;
var raio = parseFloat(input);

var A = pi * raio ** 2;

console.log(A.toFixed(4));