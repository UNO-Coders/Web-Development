function main(){
    const hrhand = document.querySelector('.hrs')
    const minhand = document.querySelector('.mins')
    const sechand = document.querySelector('.secs')
    const millihand = document.querySelector('.milli')
    var a = new Date();
    var hrs = a.getHours();
    var mins = a.getMinutes();
    var secs = a.getSeconds();
    var mil = a.getMilliseconds();
    var hourAngle = -hrs*15 
    var minAngle = -mins*6
    var secAngle = -secs*6 
    var milAngle = -mil*36
    console.log(hourAngle, minAngle, secAngle, milAngle)
    hrhand.style.transform = `rotate(${hourAngle}deg)`;
    minhand.style.transform = `rotate(${minAngle}deg)`;
    sechand.style.transform = `rotate(${secAngle}deg)`;
    millihand.style.transform = `rotate(${milAngle}deg)`;
}
function start(){
    console.log("started")
    setInterval(main, 1);
}
