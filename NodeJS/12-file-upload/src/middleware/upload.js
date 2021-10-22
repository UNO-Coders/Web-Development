const util = require('util');
const multer = require('multer');
const MAX_SIZE = 10 * 1024 * 1024;

let storage = multer.diskStorage({
	destination: (req, file, cb) => {
		cb(null, __basedir + '/resources/static/assets/uploads/');
	},
	filename: (req, file, cb) => {
		const fileName = `${Date.now()}${extname(file.originalname)}`;
                cb(null, fileName);
	},
});

let uploadFile = multer({
	storage: storage,
	limits: { fileSize: MAX_SIZE },
}).single('file');

let uploadFileMiddleware = util.promisify(uploadFile);

module.exports = uploadFileMiddleware;
