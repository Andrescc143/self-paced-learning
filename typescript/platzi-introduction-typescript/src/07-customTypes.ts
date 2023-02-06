//We can create custom type to use with the variables to be created
let userID: string | number;

//Thanks to that, we can executed the below code without problems.
userID = "Camilo";
console.log(`The UserID this time is ${userID}`);
userID = 458;
console.log(`The UserID this time is ${userID}`);

//to use a variable like this one in a function it is recommended to do
function dynamicVariable(variable: string | number) {
  if (typeof variable === 'string'){
    console.log(variable.toUpperCase());
  }
  else {
    console.log(variable.toFixed());
  }
}


//Another way would be
type UserID2 =  string | number | boolean;
let userID2: UserID2;

//Now we can executed the below code without problems
userID2 = "Hola";
userID2 = 800;
userID2 = true;


//We can create a set of possible values for a variable using literal types
//type Size = "S" | "M" | "L";
let size: Size;
