function plus(a, b) {
    return a + b;
}
function minus(a, b) {
    return a - b;
}
function multiply(a, b) {
    return a * b;
}
function divide(a, b) {
    return a / b;
}
function operate(op, a, b) {
    operations = {"+": plus,
                  "-": minus,
                  "*": multiply,
                  "/": divide,
                };

    return operations[op](a, b);
}