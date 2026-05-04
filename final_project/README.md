# Final Project

**Topic:** IoT Sensor Data Streaming & Web Visualization
**Type:** Extensive Lab / Implementation
**Description:** 

This directory contains the final project for EC 441, representing a substantial piece of work worth double the points of a regular assignment.

The project consists of an ESP32 microcontroller acting as a Wi-Fi UDP client (`station_example_main.c`) that reads I2C data from an ADXL343 accelerometer. It calculates roll and pitch and streams this data over UDP to a Node.js server (`grapher.js`). The server uses `Express` and `Socket.IO` to bridge the UDP traffic to a web client (`index.html`), where the live accelerometer and orientation data are graphed in real-time using `CanvasJS`.