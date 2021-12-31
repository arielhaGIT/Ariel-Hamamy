function advertisementPopUp() {
    let x = Math.random();
    if (x<0.25) {
       window.alert("The succulent will be beautiful in a sleeping room");
    }
    else if (x<0.5){
        window.alert("Mother did not receive such a beautiful gift for a long time");
    }
    else if (x<0.75){
        window.alert("The succulent will suit your eye color");
    }
    else{
     window.alert("You need some flower pots in the living room ...");
    }
}



var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}

