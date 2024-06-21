#!/usr/bin/node

// function that prints nmber of argument already printed
let count = 0;
exports.logMe = function(item){
    console.log(`${count}: ${item}`);
    count++;
}
