var changeHeading = function(e) {
    var h = document.getElementById("h");
    h.innerHTML = e;
};

var lis = document.getElementsByTagName("li");

for(var i = 0; i < lis.length; i++) {
    var head = lis[i];
    lis[i].addEventListener('mouseover', () => {changeHeading(head.innerHTML);});
    lis[i].addEventListener('mouseout', () => {changeHeading("Hello World!");});
    console.log(`lis[${i}]`);
};

var addItem = (e) => {
    var list = document.getElementById("thelist").inner_html;
};
