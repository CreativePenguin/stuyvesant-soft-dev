var canvas = document.getElementById("bobross");
var ctx = canvas.getContext('2d');
var dot_type = document.getElementById("buildabear");

var jolteon = function() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
};

var flareon = function() {
    console.log("Down With the Anarchy! All Hail Democracy!");

    canvas.getBoundingClientRect();
    ctx.fillRectangle(x, y, 10, 10);
    if(dot_type.innerText == "draw-a-rectangle") {
        dot_type.innerText = "draw-a-circle";
    } else if(dot_type.innerText == "draw-a-circle") {
        dot_type.innerText = "draw-a-rectangle";
    } else {
        console.log("something went wrong");
    }
};

var draw = function(x, y, isRect, size) {
    var x = x - size * .5;
    var y = y - size * .5;
    if(isRect) ctx.fillRectangle(x, y, size, size);
    else {
        ctx.beginPath();
        ctx.arc(x, y, size, 0, Math.PI * 2);
        ctx.fill();
    }
};

document.getElementById("clear").addEventListener("click", () => {ctx.clearRect(0, 0, canvas.width, canvas.height);});
document.getElementById("buildabear").addEventListener("click", flareon);
canvas.addEventListener('click', (evt) => {
  console.log(`pageX: ${evt.pageX} screenX: ${evt.screenX} clientX: ${evt.clientX}`);
  console.log(`${canvas.getBoundingClientRect()}`)
});
