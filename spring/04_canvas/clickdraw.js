var canvas = document.getElementById("bobross");
var ctx = canvas.getContext('2d');
var dot_type = document.getElementById("buildabear");

var jolteon = function() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
};

var flareon = function() {
    console.log("Down With the Anarchy! All Hail Democracy!");
    
    ctx.fillRectangle(x, y, 10, 10);
    if(dot_type.innerText == "draw-a-rectangle") {
        dot_type.innerText = "draw-a-circle";
    } else if(dot_type.innerText == "draw-a-circle") {
        dot_type.innerText = "draw-a-rectangle";
    } else {
        console.log("something went wrong");
    }
};
function getMousePos(canvas, evt) {
    var rect = canvas.getBoundingClientRect();
    return {
        x: evt.clientX - rect.left,
        y: evt.clientY - rect.top
    };
}
document.getElementById("clear").addEventListener("click", jolteon);
document.getElementById("buildabear").addEventListener("click", flareon);
canvas.addEventListener("click", function(evt) {
    
});
