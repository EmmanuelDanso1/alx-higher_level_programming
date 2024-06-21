#!/usr/bin/node
// return the reverse version of a list
exports.esrever = function (list){
    let reversed_list = [];
    for (let i = list.length - 1; i >= 0; i--){
        reversed_list.push(list[i]);
    }
    return reversed_list;
}
