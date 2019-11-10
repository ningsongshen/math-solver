let container = document.querySelector(".container");

let result = document.createElement("div");
result.classList.add("result");

let number = "";
result.innerHTML = number;

container.appendChild(result);

const gridSize = 4 * 4
const symbols = [7, 8, 9, "/", 4, 5, 6, "*", 1, 2, 3, "-", 0, ".", "=", "+"]
for (i = 0; i < gridSize; i++) {
    let square = document.createElement("div");
    square.classList.add("square");

    let symbol = document.createElement("p");
    symbol.innerHTML = symbols[i]

    square.addEventListener("click", function() {
        result.innerHTML += symbol.innerHTML;
    });

    square.appendChild(symbol);
    container.appendChild(square);
}

result.addEventListener()
