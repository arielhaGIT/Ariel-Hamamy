var i = 0;
var text = "Processing your Details...";
var speed = 150;

function typeWriter() {
    if (i < text.length) {
        document.getElementById("working").innerHTML += text.charAt(i);
        i++
        setTimeout(typeWriter, speed);
    }
}

function HeadingTyping() {
    document.getElementById("working").innerHTML = "";
    typeWriter();
}