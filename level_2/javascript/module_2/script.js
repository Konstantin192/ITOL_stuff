// window.onload = function() {
//     alert("Welcome to your JavasScript Course!");
//     console.log("The web page has loaded!");
// }


function changeText() {
    var heading = document.getElementById("demo");
    heading.textContent = "New text";
}


// var myAge = 43;

// if (myAge >= 18) {
//     console.log("You are an adult.");
// }
// else {
//     console.log("You are a minor.");
// }


// var x = 10;
// var y = 20;
// var result = x + y;

// console.log(result);


var myAge = 30;

if (myAge >= 18) {
    document.getElementById("demo").style.color = "red";
}
else {
    document.getElementById("demo").style.color = "blue";
}