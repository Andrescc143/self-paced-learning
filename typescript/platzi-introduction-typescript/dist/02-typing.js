"use strict";
/*The below syntax with the arrow function is used to isolate the environment of execution of the program and create an independent scope.*/
(() => {
    //The engine is capable to identify the variable type
    let myProductName = "Product1";
    let productPrice = 43;
    //Even when the type is automatically selected by the engine, we can not use any other type of variable for each variable in the rest of the code, otherwise, it will throws an error.
    //myProductName = 456;
    //The same behavior can be seen if the placeholder is not variable but const
    const productName = "Car";
    //productName = "Car2";
})();
