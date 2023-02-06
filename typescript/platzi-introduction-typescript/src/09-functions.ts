//Using Typescript function we need to pass all the arguments defined in order to execute the function

function createObject(
  name: string,
  age: number,
  isWorking: boolean,
  //the optional chaining operation make this argument optional. If it is no passed throw the function execution, it would be undefined.
  incomes?: number
){
  return {
    name,
    age,
    isWorking,
    incomes
  }
}

//With the functiona calling, TypeScript evaluate as well the rigth types of argument is being passed.
const personOne = createObject("Camilo", 24, true);

