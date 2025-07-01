// Set stores unique values, maintains insertion order, can be looped 

const mySet = new Set(); // creating new set
mySet.add(1,2); // 2 is not added by this
mySet.add(3);
mySet.add('hey'); // can contain different type as num, string
console.log(mySet);

const set2 = new Set([1,2,3,4,'Joey']) // another way to create set
console.log(set2)

// operations on set 
const s = new Set([1,2,3,4,'Monica'])
s.add('Chandler') // Adds Chandler to s
s.delete(2) // deletes 2 from s
s.has('Chandler') // checks if chandler in set
s.size; // tells size of set
console.log(s);
s.clear();
console.log(s);

// for of loop
const colors = new Set(['red','orange','yellow','green', 'blue', 'indigo', 'violet', 'black']);
for (let color of colors){
    console.log(color);
}

colors.forEach(color => console.log(color));

// converting array to string
const num = [1,2,3,2,4,4,3,1,5,5,6];
const uniqueNums = [...new Set(num)];