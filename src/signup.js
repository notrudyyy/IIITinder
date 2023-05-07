function setCookie(name,value,days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}
function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}
function eraseCookie(name) {   
    document.cookie = name +'=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
}

window.onclick = e => {
        if (e.target.className == "signup-btn"){
            if(getCookie("login") == "true"){
                document.getElementById("error-msg").innerText = "You are already logged in!";
                return;
            }
            var usermail = document.getElementById("email_text").value;
            e.preventDefault();
            var url = "http://127.0.0.1:5000/auth-signup";
            var xhr = new XMLHttpRequest();
            xhr.open("POST", url, true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.onload = function() {
                if (xhr.status === 200) {
                    var responseJSON = JSON.parse(xhr.responseText);
                    console.log(responseJSON);
                    if (responseJSON["success"] =="true"){
                        setCookie("user_email", usermail, 1);
                        window.location = "update.html";
                    } else{
                        document.getElementById("error-msg").innerText = "This user already exists!";
                        return;
                    }
                }
            };
            xhr.send(JSON.stringify({
                first_name:document.getElementById("first_name_text").value,
                last_name:document.getElementById("last_name_text").value,
                age:document.getElementById("age_text").value,
                phone_no:document.getElementById("phone_no_text").value,
                email:document.getElementById("email_text").value,
                password:document.getElementById("password_text").value
            }));
        }
    }