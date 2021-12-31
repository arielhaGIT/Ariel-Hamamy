
function UpdateDetailsvalidateForm() {
    let name = document.forms["UpdateDetails"]["username"].value;
    if (name.length < 3) {
        alert("The name you choose is too short");
        return false;
    }
    if (/\d/.test(name)) {
        alert("un-valid name it is impossible to use numbers");
        return false;
    }
    let pas = document.forms["UpdateDetails"]["password"].value;
    if (pas.length < 4) {
        alert("The password is too short");
        return false;
    }
    let pas2 = document.forms["UpdateDetails"]["password2"].value;
    if (pas != pas2) {
        alert("your passwords are not equal");
        return false;
    }
    let email = document.forms["UpdateDetails"]["email"].value;
    let atposition=email.indexOf("@");
    let dotposition=email.lastIndexOf(".");
    if (atposition<1 || dotposition<atposition+2 || dotposition+2>=email.length){
        alert("un-valid email");
        return false;
    }
}

function UpdateDetailsvalidateForm() {
    let name = document.forms["UpdateDetails"]["username"].value;
    if (name.length < 3) {
        alert("The name you choose is too short");
        return false;
    }
    if (/\d/.test(name)) {
        alert("un-valid name it is impossible to use numbers");
        return false;
    }
    let pas = document.forms["UpdateDetails"]["password"].value;
    if (pas.length < 4) {
        alert("The password is too short");
        return false;
    }
    let pas2 = document.forms["UpdateDetails"]["password2"].value;
    if (pas != pas2) {
        alert("your passwords are not equal");
        return false;
    }
    let email = document.forms["UpdateDetails"]["email"].value;
    let atposition=email.indexOf("@");
    let dotposition=email.lastIndexOf(".");
    if (atposition<1 || dotposition<atposition+2 || dotposition+2>=email.length){
        alert("un-valid email");
        return false;
    }
}