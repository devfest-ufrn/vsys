function hasSpecialCharacters(str) {
    var expr = /[*\\/|<>\"?:]/g;
    if (str.search(expr) > 0)
        return true;
    else
        return false;
}

function validate(fieldname) {
    var field = document.getElementById(fieldname);
    var message = document.getElementById(fieldname + "Mes");
    message.style.display = "inline-block";
    
    if (field.value == "") {
        message.innerHTML = "This field must be filled";
    } else if (field.value.includes(" ")) {
        message.innerHTML = "No spaces are allowed in this field";
    } else if (hasSpecialCharacters(field.value)) {
        message.innerHTML = "No special characters are allowed on this field";
    } else if (fieldname == "email" && field.value.indexOf("@") == -1) {
        message.innerHTML = "Please input a valid email";
    } else {
        message.innerHTML = "✓";
        message.style.color = "green";
        return true;
    }
    message.style.color = "red";
    return false;
}

function checkPassword() {
    var pass = document.getElementById("password");
    var cpass = document.getElementById("cpassword");
    var passmes = document.getElementById("cpasswordMes");
    passmes.style.display = "inline-block";
    
    if (cpass.value != pass.value) {
        passmes.innerHTML = "Passwords don't match";
        passmes.style.color = "red";
    } else {
        passmes.innerHTML = "✓";
        passmes.style.color = "green";
    }
    
    return cpass.value == pass.value;
}

$(document).ready(function(){
    
    $("#register").click(function(){
        checkPassword();

        data = {
            'first_name': $("#first_name").val(), 
            'last_name': $("#last_name").val(),
            'email': $("#email").val(),
            'password':  $("#password").val(),
        }
        $.ajax({
            url: '/users',
            method: 'POST',
            data: data,
            context: this
        }).done(function(resp){
            if(resp.success){
                window.location.href = "/login";
            }
        });
    });
});