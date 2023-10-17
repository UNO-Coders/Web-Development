let result = document.getElementById("result");

function appendToResult(value) {
    result.value += value;
}

function clearResult() {
    result.value = "";
}

function deleteChar() {
    result.value = result.value.slice(0, -1);
}

function calculateResult() {
    let expression = result.value;
    if (expression.includes('x')) {
        expression = expression.replace(/x/g, '*');
    }
    result.value = eval(expression);
}
