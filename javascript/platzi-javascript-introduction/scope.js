var numGlobal = 20;

localScope();

/*The below console.log message will throws and error because the numLocal variable does not exit in the Global scope, only in the local scope of the function localScope
console.log(`This is the variable from the local scope: ${numLocal}`);*/

function localScope(){
    var numLocal = 30;

    console.log(`This is the variable from the global scope: ${numGlobal}`);
}