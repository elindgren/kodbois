var path = require('path');
let {PythonShell} = require('python-shell');
const PORT = process.env.PORT || 5000;  // Use the env port if available
const express = require('express');
const app = express();

app.get('/', (req, res) => {
   res.sendFile(path.join(__dirname + '/skalen.html'));
});

//If request for Python code is sent
app.get('/test', testPython);

const server = app.listen(PORT, () => {
    console.log(`Express running → PORT ${server.address().port}`);
});

function testPython(req, res) {
    var options = {
        args: [
            req.query.length // length of name
        ]
    };
    console.log(options);
    PythonShell.run(path.join(__dirname + '/slumpnamn.py'), options, function(err,data)
    {
       if (err) res.send(err);
       console.log(data);
       res.send(JSON.parse(data))
    });
}




