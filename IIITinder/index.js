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

var form = document.getElementById("review_form");
form.addEventListener('submit', displaying);

function displaying(event) {
  event.preventDefault();
  
  var name = document.getElementById('name').value;
  var review = document.getElementById('review').value;
   

  var dictionary = { name: name, review: review};

  var data = localStorage.getItem('data');
  if(!data)
  {
    data = [];
  }
  else
  {
    data = JSON.parse(data);
  }

  data.push(dictionary);
  localStorage.setItem('data', JSON.stringify(data));
  displayData(data);
};

function displayData(data){
  var info = document.getElementById('data');
  info.innerHTML = '';

  for(var i=0; i<data.length; i++)
  {
    var str = "<tr><td>" + data[i].name + " says " + "\"" + data[i].review ;
    info.innerHTML += str;
  }
}

window.onbeforeunload = function() {
  localStorage.clear();
}