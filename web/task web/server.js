var express = require('express');
var app = express();

var flag = [

    {
        ID: 'flaG',
        name: 'kvvu{Light_A_P_I}'
    }
];

app.get('/', function(req, res){
    res.send('It`s API!');
})

app.get('/flag', function(req, res){
    res.send(flag);
})

app.get('/flag/:ID', function(req,res){
    console.log(req.params);
    var flag = flag.find(function(flag){
        return flag.ID === Number(req.params.ID)
    });
    res.send(flag);
})

app.listen(8080, function(){
    console.log('Api app started');
})
