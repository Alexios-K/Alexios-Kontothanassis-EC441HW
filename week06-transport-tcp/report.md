# Week 6 Report: Comparing Transport Layer Protocols

**Topic:** TCP vs. UDP and Modern Evolutions (QUIC)  
**Layer:** Transport  
**Type:** Report  

## 1. Introduction
The Transport Layer is responsible for end-to-end communication and error recovery. While the Network Layer gets a packet to the right computer, the Transport Layer ensures it gets to the right application and determines how "reliable" that delivery needs to be. The two primary protocols used for this are TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).

## 2. TCP: The Reliable Workhorse
TCP is a connection-oriented protocol designed for accuracy.

* **The 3-Way Handshake:** Before data is sent, TCP performs a "handshake" (SYN, SYN-ACK, ACK) to ensure both parties are ready.
* **Reliability:** It uses sequence numbers and acknowledgments. If a packet is lost, TCP detects the gap and retransmits it.
* **Flow & Congestion Control:** TCP dynamically slows down its transmission speed if it detects the network is becoming congested, preventing "bufferbloat".
* **Use Cases:** Web browsing (HTTP), Email (SMTP), and File Transfers (FTP).

## 3. UDP: The High-Speed Alternative
UDP is a connectionless, "fire-and-forget" protocol.

* **Minimal Overhead:** Unlike TCP, UDP has no handshake and a very small header (8 bytes vs. TCP's 20+ bytes).
* **No Guarantees:** It does not check if data arrived or if it arrived in the correct order.
* **Use Cases:** Real-time applications where speed is more important than 100% accuracy, such as VoIP, Online Gaming, and streaming data from IoT sensors (like an ESP32).

## 4. Beyond the Basics: QUIC and HTTP/3
Modern networking is shifting toward QUIC (Quick UDP Internet Connections), a protocol originally developed by Google.

* **UDP-Based:** QUIC actually runs on top of UDP to bypass the slow "middleboxes" of the internet that only understand TCP/UDP.
* **Reduced Latency:** It combines the handshake and encryption (TLS) into a single step, meaning data starts moving faster.
* **Connection Migration:** Unlike TCP, which breaks if you switch from Wi-Fi to 5G (because your IP changes), QUIC uses a "Connection ID" to keep the session alive during the transition.

## 5. Conclusion
Choosing between TCP and UDP is a trade-off between reliability and latency. While TCP remains the standard for guaranteed delivery, UDP—and modern protocols built on it like QUIC—are essential for the low-latency demands of the modern web and real-time robotics systems.