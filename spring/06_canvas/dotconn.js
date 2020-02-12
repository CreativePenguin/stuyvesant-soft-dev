var canvas = document.getElementById('playground');
var ctx = canvas.getContext('2d');

var draw = function(x, y, size) {
    x = x - size * .5;
    y = y - size * .5;
    ctx.beginPath();
    ctx.arc(x, y, size, 0, Math.PI * 2);
    ctx.fill();
};

canvas.addEventListener('click', (evt) => {
    draw(evt.pageX, evt.pageY, 5);
});
