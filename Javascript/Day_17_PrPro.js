// 1. Add 2 numbers 
let a =2;
let b = 10;
let sum = a+b;
console.log("Sum is:", sum);

// 2. Even/Odd number
let n = 11;
if (n % 2 === 0){
    console.log(n, "is even");
}
else{
    console.log(n, "is odd.");
}

//3. Print numbers 1 to 5 using loop
for (let i = 1; i<=5; i++){
    console.log(i);
}

//4. Reverse String
let str = "hello";
let rev = str.split("").reverse().join("");
console.log(rev);

//5. Even odd using for and if 
for (let i = 1; i <= 10; i++) {
  if (i % 2 === 0) {
    console.log(i + " is even");
  } else {
    console.log(i + " is odd");
  }
}

//6. Prime
for (let num =2; num<=10; num++){
    let isPr =true;

    for(let i = 2; i<=num; i++){
        if(num % i === 0){
            isPr = false;
            break;
        }
    }
    if (isPr){
        console.log(num +" is prime");
    }else{
        console.log(num +" is even");
    }
}

//7. Factorial
function fact(n){
    let res = 1;
    for (let i = 1; i<=n; i++){
        res *= i;
    }
    return res;
}
let num = 6;
console.log("Factorial of "+ num +" is: "+ fact(num));

//8. Split the string
let sentence = "Hello My Name is Ross";
let words = sentence.split(" ");
console.log(words);

//9. 
let sent = "apple,banana,cherry,grape";
let limitedSplit = sent.split(",", 2);
console.log(limitedSplit);

//10.
let sentenc = "apple123banana456cherry789";
let splitWords = sentenc.split(/\d+/); // Split by one or more digits
console.log(splitWords);

//11.
let word = "hello";
let letters = word.split("");
console.log(letters);

//12.
let sentence = "apple,banana|cherry grape";
let fruits = sentence.split(/[,| ]/); // Split by comma, pipe, or space
console.log(fruits);

//13.
let fruits = ["apple", "banana", "cherry", "apple"];
console.log(fruits[0]); 
console.log(fruits.length)

