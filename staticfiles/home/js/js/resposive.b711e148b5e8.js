function myHeader() {
    var x = document.getElementById('menu-header');
    if (x.className === 'menu') {
        x.className += ' responsive';
    } else {
        x.className = 'menu'
    }
}

window.onscroll = function () {
    myScrolltop();
}

var header = document.getElementById('menu-header');
var sticky = header.offsetTop;

function myScrolltop() {
    if (window.pageYOffset > sticky + 500) {
        header.classList.add('sticky');
    } else {
        header.classList.remove('sticky');
    }
}
// slide show
var slideIndex = 1;
// ShowSlide(ShowSlide);
function nextSlide(n) {
    ShowSlide(slideIndex += n);
}
function ShowSlide(n) {
    var i;
    var x = document.getElementsByClassName('slider-items');
    if (n > x.length) {
        slideIndex = 1;
    }
    if (n < 1) {
        slideIndex = x.length;
    }
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    x[slideIndex - 1].style.display = 'block';
}
