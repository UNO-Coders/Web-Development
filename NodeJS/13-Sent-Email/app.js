const express = require('express')
const app = express();

const { sendMail } = require('./controllers/sendMail')

app.use(express.json())

app.get('/send-mail', sendMail)

app.listen(3000, () => {
    console.log(`Ecommerce app listening on port 3000`)
})