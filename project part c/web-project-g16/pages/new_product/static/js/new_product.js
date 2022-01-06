function validation() {
    var check = 0;
    for ( let i=1; i<2; i++){
        var x = "id"+i;
        console.log(x);
        var inpObj = document.getElementById(x);
        if (!inpObj.checkValidity()) {
            check = check +1 ;
            inpObjBAD = document.getElementById(x);
            console.log(check)
        }
    }
    console.log("check is" ,check);
    if (check != 0 ){
        document.getElementById("demo").innerHTML = inpObjBAD.validationMessage;
        console.log("got into else");
    }
}