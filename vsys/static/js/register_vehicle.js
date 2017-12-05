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
    }  else { 
        message.innerHTML = "✓";
        message.style.color = "green";
        return true;
    }
    message.style.color = "red";
    return false;
}


$(document).ready(function(){
    
    $("#register").click(function(){

        data = {
            'type': $("#type").val(), 
            'brand': $("#brand").val(),
            'model': $("#model").val(),
            'year':  $("#year").val(),
            'category':  $("#category").val(),
            'color':  $("#color").val(),
            'license_plate':  $("#license_plate").val(),
            'seats':  $("#seats").val(),
            'num_doors':  $("#num_doors").val(),
            'fuel':  $("#fuel").val(),
            'value':  $("#value").val(),
        }
        $.ajax({
            url: '/vehicles',
            method: 'POST',
            data: data,
            context: this
        }).done(function(resp){
            if(resp.success){
                window.location.href = "/offercar";
            }
        });
    });
});