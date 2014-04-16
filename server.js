var restify = require('restify');
var http = require('http');
var fs = require('fs');

var server = restify.createServer();

server.use(restify.queryParser()); // to support hotel?location=...
server.use(restify.bodyParser());

// static serving
server.get(/\/js\/?.*/, restify.serveStatic({
  directory: './js'
}));

// dynamic serving
server.get('/index/', api_getLanding);
server.post('/index/', data_post);

server.listen(8080, function() {
    console.log('%s listening at %s', server.name, server.url);
});

function api_getLanding(req, res, next) {
	// simply return the landing page	
	html = fs.readFileSync('./diff.html');
    res.writeHeader(200, {"Content-Type": "text/html"});  
    res.write(html);  
    res.end();
}


function data_post(req, res, next) {
	// simply return the landing page	
	console.log("in data post");
	console.log("urla: " + req.params.urla);
	/* debug
    res.writeHeader(200, {"Content-Type": "text/json"}); 
    var response = { "response" : req.params.urla};
    res.write(JSON.stringify(response));  
    */
    var spawn = require('child_process').spawn,
    grep  = spawn('./urlDiff.py', [req.params.urla, req.params.urlb]);

	grep.stdout.on('data', function (data) {
	  	console.log('ajax sent: ' + data);
	  	res.writeHead(200, {"Content-Type": "text/plain"});
	  	res.write(data);
	    res.end();
	});

	grep.stdin.end()
}