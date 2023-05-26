function display(val) {
    document.getElementById("textval").value += val
    document.getElementById("textval").innerHTML = document.getElementById("textval").value
}

function calculate() {

    x = document.getElementById("textval").value
    y = eval(x)
    document.getElementById("textval").value = String(y)
    document.getElementById("textval").innerHTML = document.getElementById("textval").value
}
