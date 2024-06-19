let add = (x) => (y) => x + y;

let addOne = (x) => x + 1;

let numbers = [1, 2, 3, 4, 5];

numbers.map((x) => x ** 2).filter((x) => x > 4).reduce((a, b) => a + b, 0);
