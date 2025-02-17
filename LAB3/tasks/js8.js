let i = 3;

while (i) {
  alert( i-- );//3 2 1
}
//
let i1 = 0;
while (++i1 < 5) alert( i1 );//1 to 4

let i2 = 0;
while (i2++ < 5) alert( i2 );//1 to 5
//
for (let i = 2; i <= 10; i++) {
    if (i % 2 == 0) {
      alert( i );
    }
}
//
let n = 10;

nextPrime:
for (let i = 2; i <= n; i++) {

  for (let j = 2; j < i; j++) {
    if (i % j == 0) continue nextPrime; 
  }

  alert( i ); 
}