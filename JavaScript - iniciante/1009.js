var input = require('fs').readFileSync('stdin', 'utf8');
var valores = input.split('\n');

var nome = valores.shift();
var valorFixo = parseFloat(valores.shift());
var vendas = parseFloat(valores.shift());

var aReceber = vendas * 0.15 + valorFixo;

console.log("TOTAL = R$ " + aReceber.toFixed(2));