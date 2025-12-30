const baseURL = 'http://127.0.0.1:80/'

const result = document.getElementById("result");
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
function evaluateNum(num){
    if (num.includes('x')) {
        num = num.replace(/x/g, '*');
    }
    return eval(num);
}
function initilize_convertion(){
    const result = document.getElementById("result");
    var num = result.value; 
    const selectFrom = document.getElementById("selectFrom");
    const selectTo = document.getElementById("selectTo");
    // console.log(selectFrom.value)
    // console.log(selectTo.value);
    const amount = evaluateNum(num);
    // console.log(amount)
    if(amount || amount != 0){
        axios.post(baseURL+'run',{'from':selectFrom.value,'to':selectTo.value,'amount':amount}).then((value)=>{
            result.value = value?.data?.value
        }).catch((error)=>{
            result.value = 'error on converting'
        });
    }else{

    }
}