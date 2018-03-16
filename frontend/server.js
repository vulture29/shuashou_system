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

app.get('/jobs',function(req,res){
  res.render('pages/jobs');
});

app.get('/job/:job_id',function(req,res){
  res.render('pages/job_detail', {job_id: req.params.job_id});
});

app.get('/checkjobs',function(req,res){
  res.render('pages/checkjobs');
});

app.get('/checkjob/:job_id',function(req,res){
  res.render('pages/checkjob_detail', {job_id: req.params.job_id});
});

app.get('/userjobs/:wangwang_id',function(req,res){
  res.render('pages/userjobs', {wangwang_id: req.params.wangwang_id});
});

app.get('/submitjob/:job_id',function(req,res){
  res.render('pages/submit_job', {job_id: req.params.job_id});
});

app.get('/publish',function(req,res){
  res.render('pages/publish_job');
});


app.listen(3000);

console.log("Running at Port 3000");