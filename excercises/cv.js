const d = new Date();
    console.log(d);
    var h = d.getHours();
    
    if(h<12){
        greeting = "good morning";
    }else if(h<17){
        greeting = "good afternoon";
    } else{
        greeting = "good evening";
    }; console.log(greeting);

function MyName(){
    document.getElementById("Button").innerHTML= greeting;
    console.log("Ariel Hamamy");
}



