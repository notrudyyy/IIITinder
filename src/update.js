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
            e.preventDefault();
            var url = "http://127.0.0.1:5000/auth-update"
            var xhr = new XMLHttpRequest();
            xhr.open("POST", url, true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.onload = function() {
                if (xhr.status === 200) {
                    var responseJSON = JSON.parse(xhr.responseText);
                    console.log(responseJSON);
                    if (responseJSON["success"]== "true"){
                        setCookie("user_hostel", document.getElementById("hostel_data").value,1);
                        setCookie("user_desc", document.getElementById("desc_data").value,1);
                        setCookie("user_lang", document.getElementById("lang_data").value,1);
                        setCookie("user_floor", document.getElementById("floor_data").value,1);
                        setCookie("user_sleep", document.getElementById("sleep_data").value,1);
                        setCookie("user_env", document.getElementById("env_data").value,1);
                        setCookie("user_guest", document.getElementById("guest_data").value,1);
                        setCookie("user_branch", document.getElementById("branch_data").value,1);
                        setCookie("user_hobby", document.getElementById("hobby_data").value,1);
                        setCookie("user_nonveg", document.getElementById("nonveg_data").value,1);
                        setCookie("user_clean", document.getElementById("clean_data").value,1);
                        console.log(getCookie("user_hostel"));
                        console.log(getCookie("user_desc"));
                        console.log(getCookie("user_lang"));
                        console.log(getCookie("user_floor"));
                        console.log(getCookie("user_sleep"));
                        console.log(getCookie("user_env"));
                        console.log(getCookie("user_guest"));
                        console.log(getCookie("user_branch"));
                        console.log(getCookie("user_hobby"));
                        console.log(getCookie("user_nonveg"));
                        console.log(getCookie("user_clean"));
                        window.location = "matches.html";
                    }
                }
            };
            xhr.send(JSON.stringify({
                email:getCookie("user_email"),
                hostel:document.getElementById("hostel_data").value,
                desc:document.getElementById("desc_data").value,
                lang:document.getElementById("lang_data").value,
                floor:document.getElementById("floor_data").value,
                sleep:document.getElementById("sleep_data").value,
                env:document.getElementById("env_data").value,
                guest:document.getElementById("guest_data").value,
                branch:document.getElementById("branch_data").value,
                hobby:document.getElementById("hobby_data").value,
                nonveg:document.getElementById("nonveg_data").value,
                clean:document.getElementById("clean_data").value
            }));
            
        }
    }