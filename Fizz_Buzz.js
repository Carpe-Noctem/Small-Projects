/*
Simple "FizzBuzz" script written in JavaScript.
*/

var numList = [];

var count = 1;

while (count <= 100) {
    numList.push(count);
    count++;
}

for (var n = 0; n < numList.length; n++) {
    if (numList[n] % 3 === 0 && numList[n] % 5 === 0) {
        console.log("FizzBuzz");
    }
    else if (numList[n] % 3 === 0) {
        console.log("Fizz");
    }
    else if (numList[n] % 5 === 0) {
        console.log("Buzz");
    }
    else {
        console.log(numList[n]);
    }
}
