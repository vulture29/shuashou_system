var express = require('express');
var app = express();
var ejs = require('ejs');

app.use(express.static(__dirname + '/public'));

// views is directory for all template files
app.set('views', __dirname + '/views');
app.set('view engine', 'html');
app.engine('html', ejs.__express);

app.get('/',function(req,res){
  res.render('pages/index');
});

app.get('/job',function(req,res){
  res.render('pages/job');
});


app.listen(3000);

console.log("Running at Port 3000");