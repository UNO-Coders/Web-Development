require('dotenv').config();
const { default: axios } = require('axios');
const express = require('express');
const app = express();
const httpServer = require('http').createServer(app);
const circularJSON = require('circular-json');
const PORT = process.env.PORT || 80;
const IP_ADDRESS = process.env.IP_ADDRESS || "127.0.0.1";
const API_KEY = process.env.API_KEY; // you only need to get api key from https://app.exchangerate-api.com
const path = require('path');

app.use(express.json());
app.use(express.urlencoded({extended:true}));
app.use(express.static('public'));
app.use('/static',express.static('public'));
app.get('/',(req,res)=>{
    console.log("OK")
    res.sendFile(path.join(__dirname,'public','calculator.html'))
})

app.post('/run',async (req,res)=>{
    const from = req.body.from;
    const to = req.body.to;
    const amount = req.body.amount;
    try{
        var resp = await axios.get(`https://v6.exchangerate-api.com/v6/${API_KEY}/latest/${from}`);
        resp = JSON.parse(circularJSON.stringify(resp));
        num = resp?.data?.conversion_rates[to];
        realValue = Number(num)*Number(amount);
        res.status(200).json({'value':realValue});
    }catch(error){console.log(error);res.status(404).json({"message":"error occur"})}
})

httpServer.listen(PORT,IP_ADDRESS,()=>{
    console.log('server is running')
})