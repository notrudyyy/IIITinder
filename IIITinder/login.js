window.onclick = e => {
    if (e.target.className == "signup-button"){
        var url = "http://127.0.0.1:5000/auth-login"
        var xhr = new XMLHttpRequest();
        xhr.open("POST", url, true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.responseType = 'json';
        xhr.send(JSON.stringify({
            email:document.getElementById("email_text").value,
            password:document.getElementById("password_text").value
        }));
        var responsedata;
        xhr.onreadystatechange = function() { 
            // If the request completed, close the extension popup
            if (req.readyState == 4){
                responsedata  = xhr.responseText;
            };
        };
        console.log(responsedata);
    }
}