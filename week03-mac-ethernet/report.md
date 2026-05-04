Week 3 Report: Multiple Access at the Link Layer

1. The Challenge of Shared Media
In the early days of networking, devices often shared a single physical medium (like a coaxial cable). If two devices transmitted at the same time, their signals would overlap, resulting in a collision that rendered the data unreadable. To manage this, the Carrier Sense Multiple Access with Collision Detection (CSMA/CD) protocol was developed as part of the IEEE 802.3 Ethernet standard.

2. How CSMA/CD Works
The protocol functions like a polite conversation in a dark room:

Carrier Sense (CS): Before talking, a station "listens" to the wire. If it senses a signal (a carrier wave), it waits.

Multiple Access (MA): Multiple stations are connected to the same medium and have equal right to use it once it is idle.

Collision Detection (CD): While a station is talking, it continues to listen. If it detects a different signal overlapping its own, it knows a collision has occurred.

The "Jam" and "Backoff" Process
When a collision is detected, the station immediately stops transmitting the frame and instead sends a jam signal. This ensures all other stations know a collision happened. Each station then enters an Exponential Backoff phase:

The station picks a random wait time from a range.

If another collision occurs, the range of possible wait times doubles.

This randomness prevents the same two stations from colliding again immediately.

3. The Shift to Switched Ethernet
In modern networking CSMA/CD is largely a legacy concept. Modern networks use Switched Ethernet:

Full-Duplex: Devices can send and receive at the same time on separate pairs of wires.

Micro-segmentation: Switches create a dedicated "collision domain" for each port.
Because a device is only "talking" to the switch and not sharing the wire with ten other computers, collisions are physically impossible in a full-duplex switched environment.

4. Why it Matters for Wireless (CSMA/CA)
Understanding CSMA/CD is essential for contrasting it with Wi-Fi (802.11). In wireless, a radio cannot "listen" while it is "talking" because its own transmission drowns out all other signals. Therefore, Wi-Fi uses Collision Avoidance (CSMA/CA),relying on handshakes like RTS/CTS (Request to Send/Clear to Send) to prevent collisions before they happen rather than detecting them after the fact.