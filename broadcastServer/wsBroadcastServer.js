//codini$ javascript, node.js
var ws = require("nodejs-websocket")
var request = require('request');

//Load Docsets
var docsets = {}
docsets['javascript'] = require('./docsets/javascript.json').Tokens.Token
docsets['html'] = require('./docsets/html.json').Tokens.Token
docsets['css'] = require('./docsets/css.json').Tokens.Token

//DocsetLoader
var cache = {}

function getDocset(docset, callback) {
    var url = "http://test.com/" + docset
    if (docset in cache) {
        callback(cache[docset])
    }
    request(url, function(error, response, body) {
        if (!error && response.statusCode == 200) {
            callback(body)
            cache[docset] = body
        }
    })
}

// Websocket Broadcast Server
var server = ws.createServer(function(conn) {
    console.log("New connection")
    conn.on("text", function(str) {
        server.connections.forEach(function(conn) {
            conn.sendText(str)
        })
    })
    conn.on("close", function(code, reason) {
        console.log("Connection closed")
    })
}).listen(8080)

function broadcast(str) {
    server.connections.forEach(function(conn) {
        conn.sendText(str)
    })
}


/* Main UDP Server */
var PORT = 8888;
var HOST = '0.0.0.0';

var dgram = require('dgram');
var udpServer = dgram.createSocket('udp4');

udpServer.on('listening', function() {
    var address = udpServer.address();
    console.log('UDP Server listening on ' + address.address + ":" + address.port);
});

udpServer.on('message', function(message, remote) {
    var data = JSON.parse(message)

    //Get Array of Languages
    var firstLine = data.firstLine.substring(data.firstLine.indexOf('codini$') + 'codini$'.length)
    firstLine = firstLine.replace(/\s/g, "");
    var docsetsLanguages = firstLine.split(",")
        //console.log(docsetsLanguages)
        //console.log(data)

    console.log("***********************************")

    var syntax = 'javascript'
    clear

    var possibleMatches = []

    for (index in docsets[syntax]) {
        if (docsets[syntax][index].TokenIdentifier.Name.indexOf(data.word) > -1) {
            possibleMatches.push(docsets[syntax][index])
        }
    }

    console.log(possibleMatches)
});

udpServer.bind(PORT, HOST);