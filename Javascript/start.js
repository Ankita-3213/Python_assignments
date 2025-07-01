console.log("Hello Ankita")
console.log("It feels great to learn something new")

// let: Allows block-scoped variables, as opposed to var, which is function-scoped.
let x = 10;
if (x === 10){  // === checks both value and type
    let x = 20;
    console.log(x); // 20 block value
}

console.log(x); // 10 function value

// const = Constant variavle , value cannot be changed
const y = 10;
// y = 20;   if executed throws TypeError 
console.log(y);

// for loop
for (let i = 0; i<5; i++){
    setTimeout(() => console.log(i), 2000); // => arrow function for shorter syntax
}

// Template literals = ${} - embeds expression inside string using (``) 
let per = 'Tom';
console.log(`Hello, ${per}!`);

// functions with default parameters
function greet(name = 'Guest'){
    console.log(`Hello, ${name}!` );
}
greet(); // Hello Guest
greet('Jerry'); // Hello Jerry

// destructure - values from array to a,b,c
const arr = [1, 2, 3];
const [a, b, c] = arr;
console.log(a, b, c); 

// rest operator(...): Takes multiple values 
function sum(...numbers){
    return numbers.reduce((total, num) => total + num, 0);
}
console.log(sum(1,2,3,4,5));

// spread operator(...): Expands array or object, when we want to add values in already existing array/object
const arr1 = [1,2,3];
const arr2 =[...arr1, 4,5];
console.log(arr1);
console.log(arr2);