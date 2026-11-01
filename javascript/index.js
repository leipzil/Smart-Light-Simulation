console.log("I like sushi");
console.log("It's really good!")

window.alert("I REALLY LOVE PIZZA") //pop-up

//This is a comment
/*
    This
    is
    a
    multi-line
    comment
*/

/* Two steps:
1. Declaration (var, let, const)
2. Assignment (=assignment operator)
*/

let firstname = "Levina";

let age = 21;
age = age + 1

let student = false;

console.log("Hello", firstname);
console.log("You are", age, "years old");
console.log("Enrolled", student);

document.getElementById("p1").innerHTML = "Hello " + firstname;
document.getElementById("p2").innerHTML = "You are " + age + " years old";
document.getElementById("p3").innerHTML = "Enrolled: " + student;