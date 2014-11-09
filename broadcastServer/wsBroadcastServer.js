//codini$ javascript, node.js
var ws = require("nodejs-websocket")
var request = require('request');

//Load Docsets
var docsets = {}
docsets['JavaScript'] = require('./docsets/javascript.json').Tokens.Token
docsets['HTML'] = require('./docsets/html.json').Tokens.Token
docsets['CSS'] = require('./docsets/css.json').Tokens.Token
docsets['Python 3'] = require('./docsets/python3.json').Tokens.Token

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

    console.log("***********************************")

    var tokens = data.syntax.trim().split(" ")
    var lastToken = tokens[tokens.length - 1]

    //console.log(tokens)

    var syntax = 'HTML'

    if (lastToken.indexOf("js") > -1) {
        syntax = "JavaScript"
    } else if (lastToken.indexOf("css") > -1) {
        syntax = "CSS"
    } else if (lastToken.indexOf("python") > -1) {
        syntax = "Python 3"
    }

    var possibleMatches = []

    for (index in docsets[syntax]) {
        if (docsets[syntax][index].TokenIdentifier.Name.indexOf(data.word) > -1) {
            possibleMatches.push(docsets[syntax][index])
        }
    }

    jsonData = {}
    jsonData['word'] = data.word
    jsonData['syntax'] = syntax
    jsonData['matches'] = possibleMatches

    dataString = JSON.stringify(jsonData)
    //console.log(jsonData['syntax'])
    broadcast(dataString)
});

udpServer.bind(PORT, HOST);