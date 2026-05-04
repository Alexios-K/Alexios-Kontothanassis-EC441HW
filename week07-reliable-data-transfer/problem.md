# Artifact: Reliable Data Transfer (RDT) Analysis

**Topic:** Reliable data transfer: Stop-and-Wait, sliding window (GBN, SR)  
**Layer:** Transport  
**Type:** Problem  

## Problem 1: Stop-and-Wait Efficiency
Assume a satellite link with a 1 Gbps transmission rate and a round-trip time (RTT) of 100 ms. You are sending packets of 1,000 bytes using a simple Stop-and-Wait protocol.

Calculate the utilization ($U_{sender}$) of the sender.

### Solution:
First, calculate the transmission time ($d_{trans}$):

$$d_{trans} = \frac{L}{R} = \frac{1,000 \text{ bytes} \times 8 \text{ bits/byte}}{10^9 \text{ bits/sec}} = 0.000008 \text{ sec} = 8 \mu s$$

Now, calculate utilization:

$$U_{sender} = \frac{d_{trans}}{RTT + d_{trans}} = \frac{0.000008}{0.100 + 0.000008} \approx 0.00008$$

**Conclusion:** The sender is only busy 0.008% of the time. This demonstrates why Stop-and-Wait is highly inefficient for high-speed, long-distance links.

---

## Problem 2: Go-Back-N (GBN) vs. Selective Repeat (SR)
Suppose you have a window size of $N=4$ and packets 0, 1, 2, 3 are sent. Packet 1 is lost in transit. Describe the behavior of GBN versus SR when the timeout for packet 1 occurs.

### Solution:

* **Go-Back-N (GBN):** 
  The sender will retransmit packet 1 and all subsequent packets in the window (2 and 3), even if the receiver already buffered them. The receiver discards any out-of-order packets.

* **Selective Repeat (SR):** 
  The sender will retransmit only packet 1. The receiver keeps packets 2 and 3 in its buffer and waits for the retransmitted packet 1 to "fill the gap" before delivering them to the upper layer.