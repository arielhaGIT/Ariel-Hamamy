function filterupdate(c) {
  var x, i;
  x = document.getElementsByClassName("inputUpdate");
  // Add the "hide" class (display:block) to the filtered elements, and remove the "show" class from the elements that are not selected
  for (i = 0; i < x.length; i++) {
    w3AddClass(x[i], "hide");
    if (x[i].className.indexOf(c) == 1) w3RemoveClass(x[i], "hide");
  }
}


