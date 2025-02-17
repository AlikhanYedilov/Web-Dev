let d1 = new Date(2012, 1, 20, 3, 12);
alert( d1 );
//
function getWeekDay(date) {
    let days = ['SU', 'MO', 'TU', 'WE', 'TH', 'FR', 'SA'];
  
    return days[date.getDay()];
}
  
let date = new Date(2014, 0, 3); 
alert( getWeekDay(date) );
//
function getLocalDay(date) {

    let day = date.getDay();
  
    if (day == 0) {
        day = 7;
    }
  
    return day;
}
//
function getLastDayOfMonth(year, month) {
    let date = new Date(year, month + 1, 0);
    return date.getDate();
}
  
alert( getLastDayOfMonth(2012, 0) );
alert( getLastDayOfMonth(2012, 1) );
alert( getLastDayOfMonth(2013, 1) );
//
function getSecondsToday() {
    let d = new Date();
    return d.getHours() * 3600 + d.getMinutes() * 60 + d.getSeconds();
}
alert( getSecondsToday() );
//
function getSecondsToTomorrow() {
    let now = new Date();
    let hour = now.getHours();
    let minutes = now.getMinutes();
    let seconds = now.getSeconds();
    let totalSecondsToday = (hour * 60 + minutes) * 60 + seconds;
    let totalSecondsInADay = 86400;
  
    return totalSecondsInADay - totalSecondsToday;
}