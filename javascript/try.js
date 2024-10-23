// JavaScript code for demonstration
var email = "dansozipporahoforiwaa@gmail.com"; // Corrected the typo in "gmail"
var age = 35;
var male = false;

let name = "Prince Awuah Baffour"; // Using let for variable declaration
name = "Jay"; // Override previous name

const PI = 3.142; // Declaring a constant

// Single line comment in JavaScript

/*
    Block comment in JavaScript
*/
console.log(email);

// You can vote in this election if you are 18 and above
if(age >= 18){
    console.log("This user can vote because he is " + age);
}
else{
    console.log("You are too young");
}

let ans = add();

console.log(ans);

function add(){ // Functions in JavaScript
    let a = age;
    let b = 10;

    if(true){
        let localAge = 50; // Block-scoped variable, does not affect the outer 'age'
        console.log(localAge);  
    }

    return a + b;
}

console.log(age);
ans = add();
console.log(ans); // How to print something in JavaScript
