var canvas = document.getElementById("bobross");
var ctx = canvas.getContext('2d');
//var height = document.getElementById("bobross").height;

var jolteon = function() {
    ctx.clearRect()
}

var flareon = function() {
    console.log("Down With the Anarchy! All Hail Democracy!");
}

document.getElementById("clear").addEventListener("click", jolteon);
document.getElementById("buildabear").addEventListener("click", flareon);