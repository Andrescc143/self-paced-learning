//The any type is a way in which we can indicates the program the variable can have any type, however, this means the advantages of typescript won't be taken.
let variableOne: any = 400;
variableOne = "Ahora soy un string";
console.log("The variable is :" + variableOne);
//Use any is not recommended, so, in a real software development environment, avoid to use it.

//In order to get back the TypeScript advantages, we can make a casting process over the variable:
const variableStatic = variableOne as string;
//or
const variableStatic2 = <string>variableOne;
