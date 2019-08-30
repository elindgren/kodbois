var http = require('http');
var path = require('path');
const PORT = process.env.PORT || 5000;  // Use the env port if available
const express = require('express');
const app = express();

app.get('/', (req, res) => {
   res.sendFile(path.join(__dirname + '/index.html'));
});

const server = app.listen(PORT, () => {
    console.log(`Express running → PORT ${server.address().port}`);
});

