var fib = function(n) {
    if(n == 0) return 0;
    if(n == 1) return 1;
    //if(n == 2) return 1;
    return fib(n - 1) + fib(n - 2);
}

var gcd = function(a, b) {
    if(a < b) return gcdh(a, b, a);
    if(b < a) return gcdh(a, b, b);
}

var gcdh = function(a, b, c) {
    if(c <= 1) return 1;
    if(a % c && b % c) return c;
    return gcdh(a, b, c - 1);
}

var rand = function((list) {
    return list[Math.random() * list.length + 1];
}

