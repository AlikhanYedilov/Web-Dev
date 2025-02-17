min(2, 5) == 2
min(3, -1) == -1
min(1, 1) == 1

function min(a, b) {
    if (a < b) return a;
    else return b;
}
///

//pow(3, 2) = 3 * 3 = 9
//pow(3, 3) = 3 * 3 * 3 = 27
//pow(1, 100) = 1 * 1 * ...* 1 = 1
function pow(x, n) {
    let result = x;
  
    for (let i = 1; i < n; i++) {
        result *= x;
    }
  
    return result;
}