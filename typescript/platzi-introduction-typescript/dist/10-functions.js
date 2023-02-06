"use strict";
(() => {
    //We can specify the output type of a function
    const countAll = (prices) => {
        let total = prices.reduce((a, b) => { return a + b; });
        return total;
    };
    console.log(countAll([1, 2, 3, 4]));
    console.log(countAll([4, 3, 2, 1]));

    //To create void functions
    const printTotal = (prices) => {
        let total = prices.reduce((a, b) => { return a + b; });
        console.log(total);
    };

    printTotal([1, 2, 3, 4]);
})();
