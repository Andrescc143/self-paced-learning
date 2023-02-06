/* Here we are using a variable before its declaration, in these cases, JavaScript will create the corresponding variable (declaration) as an undefined variable. Thus, the console.log below will through a "undefined" message*/

console.log(`This is the value of the variable firstName calling it before assignment: ${firstName}`);

var firstName = "Andrés Camilo";

//After we re-assign a new value for the same variable, we can access to it as usual
console.log(`This is the real value for the firstName variable ${firstName}`);


//With the functions, we will see the correct behavior, however, it is important to point out we need to use in its local scope, only variable already defined, otherwise, we will receive the Undefined message saw before.
greeting();

function greeting() {
    console.log("Hola from the greeting function");
}