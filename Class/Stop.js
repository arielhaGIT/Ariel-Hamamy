var imgsarr = [
    "facebook.png",
    "instanew.jpg",
];

var i=0;

function Play(){
    setTimeout(function(){
        document.getElementById("img").src=imgs[i];
        i++
        if(i< imgsarr.length){
            play();
        } else{
            i=0;
        };

    }, 500);
}

var person = {
    firstName = "Alma",
    LastName = "Saham",
    FullName : function() {
        var Full = this.firstName +  " " + this.LastName;
    }
};

console.log(person.FullName());

