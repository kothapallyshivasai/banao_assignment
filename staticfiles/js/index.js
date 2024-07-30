function validatePasswords(event) {
    var password1 = document.getElementById('password1').value;
    var password2 = document.getElementById('password2').value;

    if (password1 !== password2) {
        event.preventDefault();
        swal("Error", "Passwords don't match", "error");
    }
}

function fields_check(event){
    username = document.getElementById("username").value
    password = document.getElementById("password").value
    if(username == "" || password==""){
        event.preventDefault()
        swal("Error!", "Fill all your Details!", "error");
    }
}