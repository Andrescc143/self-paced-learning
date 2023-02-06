"use strict";
(() => {
    //let num: number = undefined;
    //let str: string = null;
    //When we create a variable assigning null or undefined as value, the type will be Any
    let myNull = null;
    let myUndefined = undefined;
    //If we need a variable of a certain type, but we need to make the initialization as null, we can do the following
    let myNumber = null;
    //apply to function, we'll have
    function concatenar(name) {
        let greeting = "Hi";
        if (name) {
            greeting += name;
        }
        else {
            greeting += "nobody";
        }
        console.log(greeting);
    }
    //We can implement the same previous thing shorter using the below tool
    function concatenarOptimized(name) {
        let greeting = "Hi";
        //The optional chaining operator evaluates if the method can be apply depending of the variable type, and if no, we concat instead the "nobody" string.
        greeting += (name === null || name === void 0 ? void 0 : name.toLowerCase()) || "nobody";
        console.log(greeting);
    }
    concatenarOptimized(null);
    concatenarOptimized("Camilo");
    concatenar(null);
    concatenar("Andrés");
})();
