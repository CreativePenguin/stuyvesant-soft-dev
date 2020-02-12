var canvas = document.getElementById('playground');
var ctx = canvas.getContext('2d');
var clear_butt = document.getElementById('clear');

var draw = function(x, y, size) {
    x = x - size * .5;
    y = y - size * .5;
    ctx.beginPath();
    ctx.arc(x, y, size, 0, Math.PI * 2);
    ctx.fill();
};

clear_butt.addEventListener('click', () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
});
canvas.addEventListener('click', (evt) => {
    draw(evt.pageX, evt.pageY, 5);
});
