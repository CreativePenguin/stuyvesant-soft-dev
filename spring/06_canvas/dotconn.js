var canvas = document.getElementById('playground');
var ctx = canvas.getContext('2d');
var clear_butt = document.getElementById('clear');
var prevX = -1;
var prevY = -1;

var draw = function(mouseX, mouseY, size) {
    x = mouseX - canvas.getBoundingClientRect().left;
    y = mouseY - canvas.getBoundingClientRect().top;
    x = x - size * .5;
    y = y - size * .5;
    console.log(`(${x}, ${y})`);

    ctx.beginPath();
    ctx.arc(x, y, size, 0, Math.PI * 2);
    ctx.fill();

    ctx.beginPath();
    if(prevX != -1) {
        console.log('line drawn');
        ctx.moveTo(x, y);
        ctx.lineTo(prevX, prevY);
        ctx.stroke();
    }
    prevX = x;
    prevY = y;
};

clear_butt.addEventListener('click', () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
});
canvas.addEventListener('click', (evt) => {
    console.log(evt.clientX, evt.clientY);
    draw(evt.clientX, evt.clientY, 5);
});
