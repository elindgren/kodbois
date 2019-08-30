var http = require('http')
const PORT = process.env.PORT || 5000;  // Use the env port if available


http.createServer(onRequest).listen(PORT);
console.log('Server has started on port ' + PORT);

function onRequest(request, response){
    response.writeHead(200);
    response.write('Hello World');
    response.end();
}