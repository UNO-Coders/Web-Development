const cors = require('cors');
const express = require('express');
const app = express();

global.__basedir = __dirname;

app.use(
	cors({
		origin: 'http://localhost:3000',
	})
);

const initRoutes = require('./src/routes');

app.use(express.urlencoded({ extended: true }));

initRoutes(app);

let PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
	console.log(`Running at localhost:${PORT}`);
});
