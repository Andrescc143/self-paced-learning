"use strict";
//We can use the explicit syntax in order to indicate all the possible type of values the array can store
let mixedList = [1, 2, 3, true];
mixedList.push("hola");
//Otherwise, it won't store a different type
let strictMixedList = [1, 2, 3, false];
strictMixedList.push("hola");
