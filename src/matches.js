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

var matchdata = [];
var currmatch = 0;

function getHostel(hostel){
    if (hostel == "bakul"){
        return "Bakul";
    } else if (hostel == "parijaat-a"){
        return "Parijaat A";
    } else if (hostel == "parijaat-b"){
        return "Parijaat B";
    } else if (hostel == "parijaat-c"){
        return "Parijaat C";
    } else{
        return "OBH";
    }
}

function getLang(lang){
    if (lang == "eng"){
        return "English";
    } else if (lang == "tam"){
        return "Tamil";
    } else if (lang == "tel"){
        return "Telugu";
    } else if (lang == "hin"){
        return "Hindi";
    } else if (lang == "urdu"){
        return "Urdu";
    } else if (lang == "bengali"){
        return "Bengali";
    } else if (lang == "punjabi"){
        return "Punjabi";
    } else if (lang == "mall"){
        return "Malyali";
    } else{
        return "Don't Care";
    }
}

function getFloor(floor){
    if (floor == "1"){
        return "1st Floor";
    } else if (floor == "2"){
        return "2nd Floor";
    } else if (floor == "3"){
        return "3rd Floor";
    } else if (floor == "4"){
        return "4th Floor";
    } else if (floor == "5"){
        return "5th Floor";
    } else{
        return "Don't Care";
    }
}

function getSleep(sleep){
    if (sleep == "1"){
        return "At Night";
    } else if (sleep == "2"){
        return "Past Midnight";
    } else{
        return "During the Day";
    }
}

function getEnv(env){
    if (env == "1"){
        return "Silent";
    } else if (env =="2"){
        return "Music";
    } else{
        return "Noisy";
    }
}

function getGuests(guest){
    if (guest == "1"){
        return "Ok";
    } else{
        return "Not Ok";
    }
}

function getNonVeg(nonveg){
    if (nonveg == "1"){
        return "Ok";
    } else {
        return "Not OK";
    }
}

function getClean(clean){
    if (clean == "1"){
        return "Clean";
    } else if (clean == "1"){
        return "Average";
    } else{
        return "Messy";
    }
}

function compare( a, b ) {
    if ( a["matchpercent"] < b["matchpercent"] ){
      return 1;
    }
    if ( a["matchpercent"] > b["matchpercent"] ){
      return -1;
    }
    return 0;
}

function getUserMatches(){
    var url = "http://127.0.0.1:5000/get-matches"
    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
        if (xhr.status === 200) {
            var responseJSON = JSON.parse(xhr.responseText);
            console.log(responseJSON);
            if (responseJSON["success"]== "true"){
                var results = responseJSON["matches"];
                for (var i=0;i<results.length;i++){
                    if(results[i]["email"] == getCookie("user_email")){
                        continue;
                    }
                    var percent = 0;
                    if(results[i]["lang"] == getCookie("user_lang")){
                        percent++;
                    }
                    if(results[i]["floor"] == getCookie("user_floor")){
                        percent++;
                    }
                    if(results[i]["sleep"] == getCookie("user_sleep")){
                        percent++;
                    }
                    if(results[i]["env"] == getCookie("user_env")){
                        percent++;
                    }
                    if(results[i]["guests"] == getCookie("user_guest")){
                        percent++;
                    }
                    if(results[i]["branch"] == getCookie("user_branch")){
                        percent++;
                    }
                    if(results[i]["non-veg"] == getCookie("user_nonveg")){
                        percent++;
                    }
                    if(results[i]["room-desc"] == getCookie("user_clean")){
                        percent++;
                    }
                    percent = percent*100/8;
                    results[i]["matchpercent"] = percent;
                    matchdata.push(results[i]);
                }
                matchdata.sort( compare );
                document.getElementById("match-name-data").innerText = matchdata[currmatch]["first_name"]+" "+matchdata[currmatch]["last_name"];
                document.getElementById("match-age-data").innerText = matchdata[currmatch]["age"];
                document.getElementById("match-hostel-data").innerText = getHostel(matchdata[currmatch]["hostel"]);
                document.getElementById("match-desc-data").innerText = matchdata[currmatch]["desc"];
                document.getElementById("match-lang-data").innerText = getLang(matchdata[currmatch]["lang"]);
                document.getElementById("match-floor-data").innerText = getFloor(matchdata[currmatch]["floor"]);
                document.getElementById("match-sleep-data").innerText = getSleep(matchdata[currmatch]["sleep"]);
                document.getElementById("match-env-data").innerText = getEnv(matchdata[currmatch]["env"]);
                document.getElementById("match-guest-data").innerText = getGuests(matchdata[currmatch]["guests"]);
                document.getElementById("match-branch-data").innerText = matchdata[currmatch]["branch"];
                document.getElementById("match-hobby-data").innerText = matchdata[currmatch]["hobby"];
                document.getElementById("match-nonveg-data").innerText = getNonVeg(matchdata[currmatch]["non-veg"]);
                document.getElementById("match-clean-data").innerText = getClean(matchdata[currmatch]["room-desc"]);
                document.getElementById("match-percent").innerText = Math.floor(matchdata[currmatch]["matchpercent"])+"% match";
            }
        }
    };
    xhr.send(JSON.stringify({
        hostel:getCookie("user_hostel")
    }));
    
}

window.onload = function() {
    getUserMatches();
};

window.onclick = e => {
    if (e.target.className == "reject-btn" || e.target.className == "reject-btn-img"){
        console.log("testing");
        currmatch++;
        if (currmatch < matchdata.length){
            document.getElementById("match-name-data").innerText = matchdata[currmatch]["first_name"]+" "+matchdata[currmatch]["last_name"];
            document.getElementById("match-age-data").innerText = matchdata[currmatch]["age"];
            document.getElementById("match-hostel-data").innerText = getHostel(matchdata[currmatch]["hostel"]);
            document.getElementById("match-desc-data").innerText = matchdata[currmatch]["desc"];
            document.getElementById("match-lang-data").innerText = getLang(matchdata[currmatch]["lang"]);
            document.getElementById("match-floor-data").innerText = getFloor(matchdata[currmatch]["floor"]);
            document.getElementById("match-sleep-data").innerText = getSleep(matchdata[currmatch]["sleep"]);
            document.getElementById("match-env-data").innerText = getEnv(matchdata[currmatch]["env"]);
            document.getElementById("match-guest-data").innerText = getGuests(matchdata[currmatch]["guests"]);
            document.getElementById("match-branch-data").innerText = matchdata[currmatch]["branch"];
            document.getElementById("match-hobby-data").innerText = matchdata[currmatch]["hobby"];
            document.getElementById("match-nonveg-data").innerText = getNonVeg(matchdata[currmatch]["non-veg"]);
            document.getElementById("match-clean-data").innerText = getClean(matchdata[currmatch]["room-desc"]);
            document.getElementById("match-percent").innerText = Math.floor(matchdata[currmatch]["matchpercent"])+"% match";
        } 
        else{
            document.getElementById("no-matches").style.opacity = 1;
            document.getElementById("no-matches").style.zIndex = 100;
            // currmatch--;
        }
    }
    else if (e.target.className == "accept-btn" || e.target.className == "accept-btn-img"){
        document.getElementById("match-email").innerText = "Email: "+matchdata[currmatch]["email"];
        document.getElementById("match-phone").innerText = "Phone No.: "+matchdata[currmatch]["number"];
        document.getElementById("match-details").style.opacity = 1;
        document.getElementById("match-details").style.zIndex = 100;
    }
    else if (e.target.className == "close-match-details"){
        document.getElementById("match-details").style.opacity = 0;
        document.getElementById("match-details").style.zIndex = 0;
    }
}