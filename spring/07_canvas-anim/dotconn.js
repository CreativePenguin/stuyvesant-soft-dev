var canvas = document.getElementById('playground');
var ctx = canvas.getContext('2d');
var start_butt = document.getElementById('start');
var stop_butt = document.getElementById('stop');
var start = null;
var radius = 0;

var drawCircle = function(timestamp) {
  if(!start) start = timestamp;
  var progress = start - timestamp;
  if(progress < 5) {
    window.requestAnimationFrame(drawCircle)
  }
  drawCircleH(radius);
  radius += 1;
}

var drawCircleH = function(radius) {
  ctx.beginPath();
  ctx.arc(canvas.width / 2, canvas.height / 2, radius, 0, Math.PI * 2);
  ctx.fill();
}

start_butt.addEventListener('click', () => {
  console.log("press");
  window.requestAnimationFrame(drawCircle);
  radius + 1;
})
// document.addEventListener('click', () => {
//   ctx.cancelAnimationFrame();
// });
