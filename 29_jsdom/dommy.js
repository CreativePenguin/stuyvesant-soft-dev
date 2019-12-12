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
    //lis[i].setAttribute("id", `item${i}`);
    // Can't figure out how to get this code to work
    lis[i].addEventListener('mouseover', () => {
        //TODO: Change this line too -- tmp fix
        changeHeading(head.innerHTML);
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
    list.append(item);
};

var addFib = function(n) {
    
};

var addFib2 = function(n) {
    console.log(n);
    if (n == 0) return n;
    if (n == 1) return n;
    else {
        return fib(n-1) + fib(n-2);
    }
};

var b = document.getElementById("b");
b.addEventListener("click", () => {
    addItem(document.getElementById("thelist"), "WORD");
});
var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);
