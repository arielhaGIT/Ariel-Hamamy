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


function getUrlParameter(sParam)
{
    var sPageURL = window.location.search.substring(1);
    var sURLVariables = sPageURL.split('&');
    for (var i = 0; i < sURLVariables.length; i++)
    {
        var sParameterName = sURLVariables[i].split('=');
        if (sParameterName[0] == sParam)
        {
            return sParameterName[1];
        }
    }
}

function change_acording_to_querry(){
    var header = getUrlParameter('p1');
    document.getElementById('userAction').innerHTML = header;
};

