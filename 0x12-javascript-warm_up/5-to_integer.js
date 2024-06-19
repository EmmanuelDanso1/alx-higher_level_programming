#!/usr/bin/node

const args = process.argv.slice(2);
const first_arg = args[0];
const num = Number(first_arg);

if (!isNaN(num) && Number.isInteger(num)){
	console.log(`My number: ${num}`);
}else {
	console.log("Not a number");
}

