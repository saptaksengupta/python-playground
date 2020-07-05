'use strict';
// Generated By lexicon-dsa CLI tool.
// Author: Saptak Sengupta(deeps.sengupta@gmail.com)
// Github: https://github.com/saptaksengupta/

function countSquares(numberOfSides) {
    
    let counts = Array();
    counts.push(1);

    if (numberOfSides == 1) {
        return counts[0];
    }

    for (let i = 2; i <= numberOfSides; i++) {
        const nc = counts[i - 2] + (i  * i);
        counts.push(nc)
    }

    return counts[numberOfSides - 1];
}

function main() {
    let result = countSquares(3);
    console.log(result);
}

main();

