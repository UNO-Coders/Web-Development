console.log("This is the brain of Web D")

let input=document.getElementsByClassName("inp")[0];
let submit_btn=document.getElementsByClassName("btn")[0];
let res=document.getElementsByClassName("info")[0];
submit_btn.addEventListener('click',search);

function search(){
    res.style.color="black";
    let country_name=input.value;
    let url=`https://restcountries.com/v3.1/name/${country_name}?fullText=true;`;
    console.log(url);
    fetch(url)
    .then((response) => response.json())
    .then((data) => {
        let d=data[0];
            res.innerHTML=`
            <div class="info">
            <div class="img-div">
            <img src="${data[0].flags.svg}" class="img" alt="Couldn't find the flag">
            <h2>${d.name.common}</h2>
            </div>
            <h4>Continent Name : <span>${d.continents}</span></h4>
            <h4>Currency : 
            <span>
            ${data[0].currencies[Object.keys(d.currencies)].name} 
            - ${Object.keys(d.currencies)[0]}
            </span></h4>
            <h4>population : <span>${d.population}</span></h4>
            <h4>Capital : <span>${d.capital[0]}</span></h4>
            <h4>Border Country Code : <span>${d.borders.join(', ')}</span></h4>
            <h4>Time Zones : <span>${d.timezones.join(', ')}</span></h4>
            <h4>Languages : <span>${Object.values(data[0].languages).toString().split(",").join(", ")}</span></h4>
            </div>
            
            `
        }

        )
        .catch(() =>{
            res.style.fontWeight="100";
            res.style.color="red";
            if(country_name.length == 0){
                res.innerHTML =`<h4>Input field cannot be empty</h4>`;
            }
            else{
                res.innerHTML =`<h4>Please enter a valid Country Name.</h4>`;
            }    
        });
}

