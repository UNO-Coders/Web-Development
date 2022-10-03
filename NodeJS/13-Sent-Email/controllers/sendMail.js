var nodemailer = require('nodemailer');

const sendMail = (req, res) => {

    try {
        const { email, content, subject } = req.body;

        var transporter = nodemailer.createTransport({
            service: 'gmail',
            auth: {
                user: 'Add your Senders EmailId',
                pass: 'Add Your Password'
            }
        });

        var mailOptions = {
            from: 'Add Senders EmailId',
            to: "Add Recievers EmailId", //Add as a Text or an Array if u wanna Send ito multiple people
            subject: "Input Subject",
            text: "Input Content/Body",
            html: '<h1>Hi There</h1><p>Your Messsage</p>' //html page if needed
        };

        transporter.sendMail(mailOptions, function (error, info) {
            if (error) {
                res.status().json({ error: error.message })
            } else {
                res.status(200).json({ message: 'Email sent:' + info.response })
                console.log('Email sent: ' + info.response);
            }
        });

    } catch (error) {
        console.log(error)
    }
}

module.exports = { sendMail }