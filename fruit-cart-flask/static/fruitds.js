var obj;
var xhttp = new XMLHttpRequest();
     xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
       obj = JSON.parse(xhttp.responseText);
         
      }
    };
    xhttp.open("GET", "/static/fruit.json", true);
    xhttp.send(); 

 

function cart1()
  {
    var fid = 0;
    var data = obj.fruits[fid];
    console.log(data.name);
    xhttp.open("GET", '/'+fid+'/'+data.name+'/'+data.price, true);
    xhttp.send();
  }   

function cart2()
  {
    var fid = 1;
    var data = obj.fruits[fid];
    console.log(data.name);
    xhttp.open("GET", '/'+fid+'/'+data.name+'/'+data.price, true);
    xhttp.send();
  }         

function cart3()
  {
    var fid = 2;
    var data = obj.fruits[fid];
    console.log(data.name);
    xhttp.open("GET", '/'+fid+'/'+data.name+'/'+data.price, true);
    xhttp.send();
  }
function cart4()
  {
    var fid = 3;
    var data = obj.fruits[fid];
    console.log(data.name);
    xhttp.open("GET", '/'+fid+'/'+data.name+'/'+data.price, true);
    xhttp.send();
  }
function cart5()
  {
    var fid = 4;
    var data = obj.fruits[fid];
    console.log(data.name);
    xhttp.open("GET", '/'+fid+'/'+data.name+'/'+data.price, true);
    xhttp.send();
  }      