let a = +prompt("first?", "");
let b = +prompt("second?", "");

alert(a + b);
//
function readNumber(){
    let num;
    do {
        num = prompt("enter a number" , 0);
    }while(!isFinite(num));
    if(num === null || num === '') return null;
    return +num;
}
alert(`Read: ${readNumber()}`);
//
let i = 0;
while (i < 11) {
    i += 0.2;
    if (i > 9.8 && i < 10.2) alert(i);
}
//
function random(min, max) {
    return min + Math.random() * (max - min);
}
  
alert(random(1, 5));
alert(random(1, 5));
alert(random(1, 5));
//
