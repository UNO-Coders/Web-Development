
let todolist=[{ item: "Sample Item", duedate: "2023-07-07" },{ item: "Sample Item", duedate: "2023-07-07" }]


window.onload =  function(){

   let storeddata =localStorage.getItem("data");
   if (storeddata) {
      todolist = JSON.parse(storeddata);
      displayitem();}
  }
function addtodo(){
 let toditem= document.getElementById("todo")
 let itemdate= document.getElementById("datelist")
 let date = itemdate.value
 let tod = toditem.value
 
 if(tod!=""){
 todolist.push({item:tod,duedate:date});}
 
 else{
   alert("Add some item")
 }
 toditem.value =""
savetolocalstorage();
 displayitem();
}

function savetolocalstorage() {
   localStorage.setItem("data",JSON.stringify(todolist))
}


function displayitem(){
   

    let cont = document.querySelector(".todocontent")
    date=""
    
   cont.innerHTML=""
   for (let i = 0; i <todolist.length; i++) {
      let newItem = document.createElement("div");
      newItem.className ="spa"
        let{duedate,item} = todolist[i]
        newItem.innerHTML = `<span>${item}</span> <span>${duedate}</span> <button onclick="deleteitem(${i})">Delete</button>`;
        cont.appendChild(newItem);
       
    
 
   
}}
function deleteitem(i) {
    todolist.splice(i,1)
    savetolocalstorage()
    displayitem()
}

