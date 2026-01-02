var createCounter = function(n) {
    return function(){
        return n++;
    }
};

/** 
 * const counter = createCounter(10)             // This mean createCounter(10) should return a function, not a number. So that counter can become a function.
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */