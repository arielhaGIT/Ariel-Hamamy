
let txt = "Dor Hen CV Site"
let i = 0
let time = 60
function load(){
 if( i < txt.length){
    document.getElementById("head").innerHTML += txt.charAt(i);
    i++
    setTimeout(load,time);
}
}


