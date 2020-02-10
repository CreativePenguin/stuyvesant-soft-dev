var canvas = document.getElementById("central_canvas");
var ctx = canvas.getContext('2d');
var dot_butt = document.getElementById("rect_circ_toggle");
var clear_butt = document.getElementById("clear");
var canvasX = canvas.getBoundingClientRect().left;
var canvasY = canvas.getBoundingClientRect().top;
var isRect = false;

// e.preventDefault() stops the default action from happening. For instance, in the case of a textbox, the default action would be entering in text. By stopping the default action, it allows preemptive error prevention. The function only works if an event is cancellable. `Event.Cancellable` This part is speculation, but it can probably stop injection attacks.

// ctx.beginPath() differentiates between the different drawings the program makes. It is called to denote a different portion of the drawing

// e.offsetX provides the x coordinate difference between where the mouse click happened, and where the html element is located

var clear = function() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
};

var draw = function(x, y, isRect, size) {
    if(isRect) ctx.fillRect(x, y, size, size);
    else {
        x = x - size * .5;
        y = y - size * .5;
        ctx.beginPath();
        ctx.arc(x, y, size, 0, Math.PI * 2);
        ctx.fill();
    }
};

clear_butt.addEventListener('click', clear);
dot_butt.addEventListener('click', () => {
    if(isRect) {
        isRect = false;
        dot_type.innerText = "draw-a-rectangle";
    } else {
        isRect = true;
        dot_type.innerText = "draw-a-circle";
    }
});
canvas.addEventListener('click', (evt) => {
    draw(evt.pageX - canvasX, evt.pageY - canvasY, isRect, 3);
});
