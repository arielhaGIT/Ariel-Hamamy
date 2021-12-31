
//map function
function myMap() {
    var mapProp= {
        center:new google.maps.LatLng(31.19177,34.85531),
        zoom:10,
    }
    var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
}