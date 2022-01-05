
var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

var num = parseInt(lines.shift());
var hora = parseInt(lines.shift());
var salario = parseFloat(lines.shift());

var salary = hora * salario;

console.log("NUMBER = " + num);
console.log("SALARY = U$ " + salary.toFixed(2)); 