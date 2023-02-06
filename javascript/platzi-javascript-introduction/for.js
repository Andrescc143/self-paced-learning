var students = ["Camilo", "Andrés", "Lizeth", "Maria", "Davi"];

for (var i = 0; i < students.length; i++) {
    console.log("Hola " + students[i]);
}

console.log("\n");

for (var student of students) {
    console.log("Hola " + student);
}