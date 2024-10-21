let add = (x) => (y) => x + y;

let addOne = (x) => x + 1;

let numbers = [1, 2, 3, 4, 5];
let numberObjs = [{ num: 1 }, { num: 2 }, { num: 3 }, { num: 4 }, { num: 5 }];

numbers.map((x) => x ** 2).filter((x) => x > 4).reduce((a, b) => a + b, 0);

numberObjs.map((x) => ({ num: x.num ** 2 })).filter((x) => x.num > 4).reduce((a, b) => a + b.num, 0);