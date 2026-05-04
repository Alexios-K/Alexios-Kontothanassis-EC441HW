const dgram = require('dgram');
const express = require('express');
const http = require('http');
const { Server } = require("socket.io");
const path = require('path');

// --- Configuration ---
const UDP_PORT = 41234;
const HTTP_PORT = 8080;

// --- Set up Express Server ---
const app = express();
const server = http.createServer(app);

// Serve the index.html file
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// --- Set up Socket.IO Server ---
const io = new Server(server);

io.on('connection', (socket) => {
  console.log('A user connected via Socket.IO');
  socket.on('disconnect', () => {
    console.log('User disconnected');
  });
});

function broadcast(data) {
  // Emit data on a custom event that the client will listen for
  io.emit('accelerometer-data', data);
}

// --- Set up UDP Server ---
const udpServer = dgram.createSocket('udp4');

udpServer.on('error', (err) => {
  console.log(`UDP Server error:\n${err.stack}`);
  udpServer.close();
});

udpServer.on('message', (msg, rinfo) => {
  const messageStr = msg.toString();
  console.log(`UDP Server got: "${messageStr.trim()}" from ${rinfo.address}:${rinfo.port}`);

  // Parse the incoming data string
  // Format: "X: val 	 Y: val 	 Z: val\nroll: val 	 pitch: val \n"
  const match = messageStr.match(/X: ([\d.-]+)\s+Y: ([\d.-]+)\s+Z: ([\d.-]+)[\s\S]*roll: ([\d.-]+)\s+pitch: ([\d.-]+)/);

  if (match) {
    const data = {
      x: parseFloat(match[1]),
      y: parseFloat(match[2]),
      z: parseFloat(match[3]),
      roll: parseFloat(match[4]),
      pitch: parseFloat(match[5]),
      timestamp: new Date().toISOString()
    };
    // Broadcast the parsed data to all WebSocket clients
    broadcast(data); // This now uses Socket.IO
  } else {
    console.log("Could not parse incoming UDP message:", messageStr);
  }
});

udpServer.on('listening', () => {
  const address = udpServer.address();
  console.log(`UDP Server listening on ${address.address}:${address.port}`);
});

// --- Start Servers ---
udpServer.bind(UDP_PORT);
server.listen(HTTP_PORT, () => {
  console.log(`HTTP server started on http://localhost:${HTTP_PORT}`);
});