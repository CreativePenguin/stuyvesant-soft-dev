var canvas = document.getElementById("canvas");
var ctx = canvas.getContext('2d');
var clear_butt = document.getElementById("clear");
var canvasX = canvas.getBoundingClientRect().left;
var canvasY = canvas.getBoundingClientRect().top;

clear_butt.addEventListener('click', () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
});
