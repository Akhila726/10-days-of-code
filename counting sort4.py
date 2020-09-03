'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the countSort function below.
function countSort(arr) {
    let list = [];

    let maxHalf = (Math.floor(arr.length) / 2) - 1;

    for (let i = 0; i < arr.length; i++) {
        if (!(typeof list[arr[i][0]] === 'string')) {
            list[arr[i][0]] = '';
        }
        list[arr[i][0]] += (i <= maxHalf ? '- ' : arr[i][1] + ' ');
    }

    let string = '';
    for (let row = 0; row < list.length; row++) {
        if (list[row]) {
            string += list[row];
        }
    }

    console.log(string);

}

function main() {
    const n = parseInt(readLine().trim(), 10);

    let arr = Array(n);

    for (let i = 0; i < n; i++) {
        arr[i] = readLine().replace(/\s+$/g, '').split(' ');
    }

    countSort(arr);
}
