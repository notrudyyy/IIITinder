var i = 0;
var txt1 = " WELCOME TO IIITINDER - A PLACE TO FIND YOUR PERFECT ROOMMATE !!! ";
var speed = 100;

function typeWriter()
{
    if(i < txt1.length)
    {
        document.getElementById("typeheader").innerHTML += txt1.charAt(i);
        i++;
        setTimeout(typeWriter,speed);
    }
}

typeWriter();