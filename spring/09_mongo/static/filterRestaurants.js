var borough = document.getElementById("borough_select");
var zip = document.getElementById("zip_input");
var grade = document.getElementById("grade_select");
var score = document.getElementById("score_input");

var filter = function(borough, zip, grade, score) {
    
};

var pooh = function() {
    filter(borough.value, zip.value, grade.value);
};

zip.addEventListener('change', pooh);
