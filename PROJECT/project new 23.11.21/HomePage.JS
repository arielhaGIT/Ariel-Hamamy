
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

     //map function
    function myMap() {
        var mapProp= {
            center:new google.maps.LatLng(31.19177,34.85531),
            zoom:10,
        }
        var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
    }

    function SignUpvalidateForm() {
        let name = document.forms["signUp"]["username"].value;
        if (name.length < 3) {
            alert("The name you choose is too short");
            return false;
        }
        if (/\d/.test(name)) {
            alert("un-valid name it is impossible to use numbers");
            return false;
        }
        let pas = document.forms["signUp"]["password"].value;
        if (pas.length < 4) {
            alert("The password is too short");
            return false;
        }
        let pas2 = document.forms["signUp"]["password2"].value;
        if (pas != pas2) {
            alert("your passwords are not equal");
            return false;
        }
        let email = document.forms["signUp"]["email"].value;
        let atposition=email.indexOf("@");
        let dotposition=email.lastIndexOf(".");
        if (atposition<1 || dotposition<atposition+2 || dotposition+2>=email.length){
            alert("un-valid email");
            return false;
        }
    }

    function SignUpvalidateForm() {
        let name = document.forms["signUp"]["username"].value;
        if (name.length < 3) {
            alert("The name you choose is too short");
            return false;
        }
        if (/\d/.test(name)) {
            alert("un-valid name it is impossible to use numbers");
            return false;
        }
        let pas = document.forms["signUp"]["password"].value;
        if (pas.length < 4) {
            alert("The password is too short");
            return false;
        }
        let pas2 = document.forms["signUp"]["password2"].value;
        if (pas != pas2) {
            alert("your passwords are not equal");
            return false;
        }
        let email = document.forms["signUp"]["email"].value;
        let atposition=email.indexOf("@");
        let dotposition=email.lastIndexOf(".");
        if (atposition<1 || dotposition<atposition+2 || dotposition+2>=email.length){
            alert("un-valid email");
            return false;
        }
    }
    function paymentValidation() {
        let method = document.forms["paymentForm"]["Delivery_Method"].value;
        if (method == "") {
            alert("you didn't choose your delivery method");
            return false;
        }
        let Card_Number = document.forms ["paymentForm"]["Card_Number"].value;
        if (Card_Number < 1000000000000000 || Card_Number > 9999999999999999 || Card_Number == "") {
            alert("you entered an invalid card number");
            return false;
        }
        if (isallNumric(Card_Number) == false) {
            alert("you entered letters in your card number");
            return false;
        }

        let cvv = document.forms ["paymentForm"]["CVV"].value;
        if (cvv < 100 || cvv > 999 || cvv == "" || isallNumric(cvv) == false) {
            alert("you entered an invalid cvv");
            return false;
        }
    }
    function isallNumric(str){
        for (let i = 0; i < str.length; i++) {
            if (str.charAt(i) != '1' && str.charAt(i) != '2' && str.charAt(i) != '3' && str.charAt(i) != '4' && str.charAt(i) != '5' && str.charAt(i) != '6' && str.charAt(i) != '7' && str.charAt(i) != '8' && str.charAt(i) != '9'){
                return false;
            }
        }
        return true;
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
