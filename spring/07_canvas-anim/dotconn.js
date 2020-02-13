var canvas = document.getElementById('playground');
var ctx = canvas.getContext('2d');
var start_butt = document.getElementById('start');
var stop_butt = document.getElementById('stop');
var start = null;
var draw_animation = null;
var clear_animation = null;
var radius = 0;
var isExpanding = true;

var drawCircle = function(timestamp) {
  if(!start) start = timestamp;
  var progress = timestamp - start;
  if(progress % 10) {
    clear_animation = window.requestAnimationFrame(clear);
  }
  // console.log(`timestamp:${timestamp}; radius:${radius}`);
  drawCircleH(radius);
  draw_animation = window.requestAnimationFrame(drawCircle);
  if(radius <= 0) isExpanding = true;
  if(radius >= canvas.width / 2) isExpanding = false;
  radius += isExpanding ? 1 : -1;
};

var drawCircleH = function(radius) {
  ctx.beginPath();
  ctx.arc(canvas.width / 2, canvas.height / 2, radius, 0, Math.PI * 2);
  ctx.fill();
};

var clear = function() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
};

start_butt.addEventListener('click', () => {
  animation = window.requestAnimationFrame(drawCircle);
  console.log(animation);
});
stop_butt.addEventListener('click', () => {
  window.cancelAnimationFrame(draw_animation);
  window.cancelAnimationFrame(clear_animation);
});
document.getElementById('clear').addEventListener('click', () => {
  console.log(animation);
  ctx.clearRect(0, 0, canvas.width, canvas.height);
});
