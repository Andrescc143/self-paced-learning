var collection = [1, 2, 3, "Manzana", "Zanahoria"];

console.log(`I have created and array of ${collection.length} elements, and its last element is ${collection[4]}`);

//Operations with methods

//Add the element at the end of the array
collection.push("New Element"); 
console.log("Collection updated: " + collection);

//Delete and return the last element of an array
console.log(
    "\nHere is the last element (deleted) : " + collection.pop()
     + "\nAnd here is the list updated: " + collection);

//Add the element at the begining of the array
collection.unshift("New Element at the begining"); 
console.log("\nCollection updated: " + collection);

//Delete the element at the begining of the array
collection.shift(); 
console.log("\nCollection updated: " + collection);

//To find the index of an element
console.log("\n" + collection + `\nThe item '3' has index ${collection.indexOf(3)} in the array`)
