def server_js():
    return '''
let express = require('express');
let bodyParser = require('body-parser');
let mongoose = require('mongoose');
let path = require('path');
const session = require('express-session');
const flash = require('express-flash');
const app = express();
const PORT = 8000;
const db = mongoose.connection;

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
'''