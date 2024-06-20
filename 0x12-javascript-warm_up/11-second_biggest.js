#!/usr/bin/node
function second_biggest(numbers){
	if (numbers.length < 2){
		return 0;
	}
	let first = -Infinity, second = -Infinity;
	for (const num in numbers){
		if (num > first) {
			second = first;
			first = num;
		} else if (num > second){
			second = num
		}
	}
	return second;
}
const args = process.argv.slice(2).map(Numbers);
const res = second_biggest(args);
console.log(res);
