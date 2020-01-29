/**
 * @author Winston Peng
 * Softdev P9
 * K29 -- JavaScript p3
 * 2019-12-13
 */
var changeHeading = function(e) {
    var h = document.getElementById("h");
    h.innerHTML = e.target.innerHTML;
};

//alterHeading is undefined for some reason, and idk why
var alterHeading = (e) => {
    var h = document.getElementById("h");
    h.innerHTML = this.innerHTML;
};

var removeItem = function(e) {
    this.remove();
    document.getElementById("h").innerHTML = "Hello World!";
};

var lis = document.getElementsByTagName("li");

for(var i = 0; i < lis.length; i++) {

    lis[i].addEventListener('mouseover', alterHeading);
        //changeHeading(lis[this]);
        //changeHeading(lis[i].innerHTML);
    lis[i].addEventListener('mouseover', changeHeading);
    lis[i].addEventListener('mouseout', () => {
        document.getElementById("h").innerHTML = "Hello World!";
    });
    //lis[i].addEventListener('click', () => {
    //    removeItem(document.getElementById("test"));
    //});
    lis[i].addEventListener('click', removeItem);
    console.log(`lis[${i}]`);
};

var addItem = (element, value) => {
    var list = element;
    var item = document.createElement("li");
    item.innerHTML = value;
    //item.addEventListener('click', () => {
    //    removeItem(this);
    //});
    item.addEventListener('click', removeItem);
    list.append(item);
};

var ele = [0, 1];
var ele_counter = 0;
var addFib2 = function() {
    console.log(ele);
    var val = ele[0] + ele[1];
    ele[0] = ele[1];
    ele[1] = val;
    return val;
};

var addFib = function() {
    console.log(ele);
    document.getElementById("fiblist");
    addItem(document.getElementById("fiblist"), addFib2());
};

var b = document.getElementById("b");
b.addEventListener("click", () => {
    addItem(document.getElementById("thelist"), "WORD");
});
var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);
