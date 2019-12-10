var fib = function(n) {
    if(n == 0) return 0;
    if(n == 1) return 1;
    //if(n == 2) return 1;
    return fib(n - 1) + fib(n - 2);
}

var gcd = function(a, b) {
    if(a < b) return gcd(a, b, a);
    if(b < a) return gcd(a, b, b);
}

var gcd = function(a, b, c) {
    if(c <= 1) return 1;
    if(a % c && b % c) return c;
    return gcd(a, b, c - 1);
}
