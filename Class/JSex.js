var txt = "abcdefg";
var txt1=txt.length;
var txt2 = txt.slice(0,4);
console.log(txt2);
var txt3 = "come visit Microsoft!";
var txt4 = txt3.replace("Microsoft", "BGU")
console.log(txt4);

// var person = {
//     firstName = "Alma",
//     LastName = "Saham",
//     function = fullName() {
        
//     }
// }

const d = new Date();
console.log(d);
var h = d.getHours();
console.log(h);

if(h<12){
    greeting = "good morning!";
} else {
    greeting = "good evening!";
};
console.log(greeting);

function greet(){
    document.getElementById("P").innerHTML=greeting;
}

var cars = ["Toyota", "Hunda", "Ford"];
// console.log(cars[0]);
// console.log(cars[1]);

var i;
for(i=0; i<cars.length; i++){
    console.log(cars[i]);
}


