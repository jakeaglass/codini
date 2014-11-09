var ws = require("nodejs-websocket")

// Scream server example: "hi" -> "HI!!!"
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


var PORT = 8888;
var HOST = '0.0.0.0';

var dgram = require('dgram');
var udpServer = dgram.createSocket('udp4');

udpServer.on('listening', function() {
    var address = udpServer.address();
    console.log('UDP Server listening on ' + address.address + ":" + address.port);
});

udpServer.on('message', function(message, remote) {
    console.log(remote.address + ':' + remote.port + ' - ' + message);
    server.connections.forEach(function(conn) {
        conn.sendText(message)
    })
});

udpServer.bind(PORT, HOST);