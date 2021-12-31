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
        if (str.charAt(i) != '0' && str.charAt(i) != '1' && str.charAt(i) != '2' && str.charAt(i) != '3' && str.charAt(i) != '4' && str.charAt(i) != '5' && str.charAt(i) != '6' && str.charAt(i) != '7' && str.charAt(i) != '8' && str.charAt(i) != '9'){
            return false;
        }
    }
    return true;
}






