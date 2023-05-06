window.onclick = e => {
    if (e.target.className == "signup-button"){
        var url = "http://127.0.0.1:5000/auth-signup"
        var xhr = new XMLHttpRequest();
        xhr.open("POST", url, true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify({
            first_name:document.getElementById("first_name_text").value,
            last_name:document.getElementById("last_name_text").value,
            age:document.getElementById("age_text").value,
            phone_no:document.getElementById("phone_no_text").value,
            email:document.getElementById("email_text").value,
            password:document.getElementById("password_text").value
        }));
        console.log(JSON.stringify({
            first_name:document.getElementById("first_name_text").value,
            last_name:document.getElementById("last_name_text").value,
            age:document.getElementById("age_text").value,
            phone_no:document.getElementById("phone_no_text").value,
            email:document.getElementById("email_text").value,
            password:document.getElementById("password_text").value
        }));
    }
}