// Setting up the webapage
let container = document.querySelector(".container");

let result = document.createElement("div");
result.classList.add("result");

let number1 = "";
let operation = "";
let pressEqual;

result.innerHTML = number1;

container.appendChild(result);

const gridSize = 4 * 4
const symbols = [7, 8, 9, "/", 4, 5, 6, "*", 1, 2, 3, "-", 0, ".", "=", "+"]
for (i = 0; i < gridSize; i++) {
    let square = document.createElement("div");
    square.classList.add("square");

    let symbol = document.createElement("p");
    symbol.innerHTML = symbols[i]

    if (symbols[i] == ".") {
        square.classList.add("decimal");
    } else if (symbols[i] == "=") {
        square.classList.add("equal");
    } else if (["-", "+", "*", "/"].includes(symbols[i])) {
        square.classList.add("operator");
    } else {
        square.classList.add("number");
    }
    square.appendChild(symbol);
    container.appendChild(square);
}



// Adding function to the buttons
const numbers = document.querySelectorAll(".number");
displayNumber();

const decimal = document.querySelector(".decimal");
addDecimal();

const equal = document.querySelector(".equal");
calculateResult();

const operators = document.querySelectorAll(".operator");
processHalf();

function displayNumber() {
    numbers.forEach(number => {
        number.addEventListener("click", function() {
            result.innerHTML += number.querySelector("p").innerHTML;
        });
    });
}

function processHalf() {
    operators.forEach(operator => {
        operator.addEventListener("click", function() {
            equal.querySelector("p").innerHTML = "=";
            if (result.innerHTML != "") {
                number1 = Number(result.innerHTML);
                operation = operator.querySelector("p").innerHTML;
                result.innerHTML = "";
            }            
        });
    });
}

function calculateResult() {
    equal.addEventListener("click", function() {
        if (result.innerHTML != "" && equal.querySelector("p").innerHTML == "=" && operation != "") {
            let number2 = Number(result.innerHTML);
            result.innerHTML = operate(String(operation), Number(number1), Number(number2));
            equal.querySelector("p").innerHTML = "AC";
        } else if (equal.querySelector("p").innerHTML == "AC") {
            number1 = "";
            number2 = "";
            operation = "";
            result.innerHTML = "";
            equal.querySelector("p").innerHTML = "=";
        }
    })
}

function addDecimal() {
    decimal.addEventListener("click", function() {
        if (result.innerHTML.indexOf(".") == -1) {
            result.innerHTML += ".";
        }
    })
}