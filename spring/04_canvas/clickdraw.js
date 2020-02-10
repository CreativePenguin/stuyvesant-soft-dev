var canvas = document.getElementById("bobross");
var ctx = canvas.getContext('2d');
var dot_type = document.getElementById("buildabear");
var canvasX = canvas.getBoundingClientRect().left;
var canvasY = canvas.getBoundingClientRect().top;
var isRect = true;

var jolteon = function() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
};

var flareon = function() {
    console.log("Down With the Anarchy! All Hail Democracy!");

    // canvas.getBoundingClientRect();
    // ctx.fillRectangle(x, y, 10, 10);
    if(dot_type.innerText == "draw-a-rectangle") {
        dot_type.innerText = "draw-a-circle";
        isRect = false;
    } else if(dot_type.innerText == "draw-a-circle") {
        dot_type.innerText = "draw-a-rectangle";
        isRect = true;
    } else {
        console.log("something went wrong");
    }
};

var vaporeon = function(mouseX, mouseY) {
    draw(mouseX - canvasX, mouseY - canvasY, isRect, 3);
};

var draw = function(x, y, isRect, size) {
    x = x - size * .5;
    y = y - size * .5;
    if(isRect) ctx.fillRect(x, y, size, size);
    else {
        ctx.beginPath();
        ctx.arc(x, y, size, 0, Math.PI * 2);
        ctx.fill();
    }
};

console.log(`canvasX: ${canvasX} canvasY: ${canvasY}`);
document.getElementById("clear").addEventListener("click", () => {ctx.clearRect(0, 0, canvas.width, canvas.height);});
document.getElementById("buildabear").addEventListener("click", flareon);
canvas.addEventListener('click', (evt) => {
    console.log(`pageX: ${evt.pageX} screenX: ${evt.screenX} clientX: ${evt.clientX}`);
    console.log(`${canvas.getBoundingClientRect()}`);
    vaporeon(evt.pageX, evt.pageY);
});
