/**
 * @author Winston Peng
 * Softdev P9
 * K29 -- JavaScript p3
 * 2019-12-13
 */
var changeHeading = function(e) {
    document.getElementById("h").innerHTML = e;
};

var removeItem = function(e) {
    e.remove();
};

var lis = document.getElementsByTagName("li");

for(var i = 0; i < lis.length; i++) {
    //TODO: DELETE SOON -- This line just exists to stop errors
    var head = lis[i];

    // Can't figure out how to get this code to work
    lis[i].addEventListener('mouseover', () => {
        //TODO: Change this line too -- tmp fix
        changeHeading(lis[this]);
        //changeHeading(this.onmouseover.innerHTML);
        //changeHeading(lis[i].innerHTML);
        //changeHeading(document.getElementById(``).innerHTML);
    });
    lis[i].addEventListener('mouseout', () => {changeHeading("Hello World!");});
    lis[i].addEventListener('click', () => {
        removeItem(document.getElementById("test"));
    });
    console.log(`lis[${i}]`);
};

var addItem = (element, value) => {
    var list = element;
    var item = document.createElement("li");
    item.innerHTML = value;
    item.addEventListener('click', () => {
        removeItem(this);
    });
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
