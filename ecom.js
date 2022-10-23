const picChange = document.querySelector('.disp');
const opt1 = document.querySelector('.pic1');
const opt2 = document.querySelector('.pic2');
const opt3 = document.querySelector('.pic3');
const opt4 = document.querySelector('.pic4');
let numbo = document.querySelector('.num');
const cart = document.querySelector('.addCart');
const res = document.querySelector('.bugg');

let numb = parseInt(numbo.innerHTML);

const plus = document.querySelector('.pos');
const minus = document.querySelector('.neg');

plus.addEventListener('click',function() {
    numbo.innerHTML= numb+1;
    console.log(numbo);
})
minus.addEventListener('click', function() {
    numbo.innerHTML = (numbo-1);
    console.log(numbo);

})

cart.addEventListener('click', function() {
    res.setAttribute('class', 'resClick');
})


opt2.addEventListener('click', function() {
    picChange.setAttribute("src","images/image-product-2.jpg");
    opt2.setAttribute('class','onClick');
    opt1.setAttribute('class','opt');
    opt3.setAttribute('class','opt');
    opt4.setAttribute('class','opt');
})
opt3.addEventListener('click', function() {
    picChange.setAttribute("src","images/image-product-3.jpg");
    opt3.setAttribute('class','onClick');
    opt1.setAttribute('class','opt');
    opt2.setAttribute('class','opt');
    opt4.setAttribute('class','opt');

})
opt4.addEventListener('click', function() {
    picChange.setAttribute("src","images/image-product-4.jpg");
    opt4.setAttribute('class','onClick');
    opt1.setAttribute('class','opt');
    opt2.setAttribute('class','opt');
    opt3.setAttribute('class','opt');

})
opt1.addEventListener('click', function() {
    picChange.setAttribute("src","images/image-product-1.jpg");
    opt1.setAttribute('class','onClick');
    opt2.setAttribute('class','opt');
    opt3.setAttribute('class','opt');
    opt4.setAttribute('class','opt');

})

