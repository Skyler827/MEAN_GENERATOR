import sys
import os

##### STEP 1: INITIALIZE DIRECTORY #####
try:
    print(os.path.abspath(sys.argv[1]))
except: pass
# if arg is a file:
#   print error, halt
# print a message indicating we are creating an express app
# if arg is a directory:
#   remove the directory, recreate it, change to it
# if arg doesnt exist:
#   create arg as a directory, change to it
##### STEP TWO: INITIALIZE PROJECT #####
# create the following files/directories:
directories = {
    "public": {},
    "server": {
        "config": {},
        "controllers": {},
        "models": {}
    }
}
# run npm init -y in the server directory
# run npm init in the public directory
directories["server"]["server.js"] = """
let express = require('express');
let bodyParser = require('body-parser');
let mongoose = require('mongoose');
let path = require('path');
const session = require('express-session');
const flash = require('express-flash');
const app = express();
const PORT = 8000;
const db = mongoose.connection;
const UserSchema = new mongoose.Schema({
    first_name: {type: String, required: true, minlength: 6},
    last_name: {type: String, required: true, maxlength:20},
    age: {type: Number, min: 1, max: 150},
    email: {type: String, required: true}
}, {timestamps: true});

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, './static')));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
app.use(session({
    secret: 'keyboard cat',
    resave: false,
    saveUninitialized: true,
    cookie: { secure: true }
}));
app.use(flash());

mongoose.connect('mongodb://localhost/test', {useNewUrlParser:true});
mongoose.model('User', UserSchema);
const User = mongoose.model('User');

app.get('/', function(req, res) {
    res.render('index', {content:\"~_~_~_~rendered via EJS_~_~_~_\"});
})

app.listen(PORT, function() {
    console.log(\"listening on port \"+PORT);
})

"""