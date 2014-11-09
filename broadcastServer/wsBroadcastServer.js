var ws = require("nodejs-websocket")

//Load Docsets
var docsets = {}
docsets['javascript'] = require('./docsets/javascript.json').Tokens.Token
docsets['html'] = require('./docsets/html.json').Tokens.Token
docsets['css'] = require('./docsets/css.json').Tokens.Token

//Map of syntax identifiers to docset
syntaxMap = {}
syntaxMap['syntax.javascript'] = 'javascript'
syntaxMap['syntax.html'] = 'javascript'
syntaxMap['syntax.css'] = 'javascript'

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
    console.log(data)

    var syntax = 'javascript'

    var possibleMatches = []

    for (index in docsets[syntax]) {
        if (docsets[syntax][index].TokenIdentifier.Name.indexOf(data.word) > -1) {
            possibleMatches.push(docsets[syntax][index])
        }
    }

    //console.log(possibleMatches)
});

udpServer.bind(PORT, HOST);