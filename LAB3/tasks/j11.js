let user = {};

user.name = "aliko";

user.surname = "yedil";

user.name = "ali";

delete user.name;
//
function isEmpty(obj) {
    for(let i in ojb) return false;
    return true;
}
//
let salaries = {
    John: 100,
    Ann: 160,
    Pete: 130
}
let sum = salaries.John + salaries.Ann + salaries.Pete;
alert(sum);
//
function multiplyNumeric(ojb){
    for(let i in obj){
        if(typeof obj[i] == 'number') obj[i]*=2;
    }
}
//
let calculator = {
    sum(){
        return this.a + this.b;
    },
    mul(){
        return this.a * this.b;
    },
    read(){
        this.a = +prompt('a?' , 0);
        this.b = +prompt('b?' , 0);
    }
};
calculator.read();
alert(calculator.sum());
alert(calculator.mul());
///
let ladder = {
    step: 0,
    up() {
       this.step++;
       return this;
    },
    down() {
        this.step--;
        return this;
    },
    showStep() {
        alert( this.step );
        return this;
    }
};ladder.up().down().up().showStep();
//
