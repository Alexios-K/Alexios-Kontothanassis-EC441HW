import sys
import logging
# Suppress scapy IPv6 warnings if IPv6 is not heavily configured
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import IP, ICMP, sr1

def manual_traceroute(target, max_hops=30):
    print(f"Tracing route to {target} over a maximum of {max_hops} hops:\n")
    
    for ttl in range(1, max_hops + 1):
        # Craft the IP packet with the current TTL and encapsulate an ICMP Echo Request
        pkt = IP(dst=target, ttl=ttl) / ICMP()
        
        # Send the packet and wait for a single response (timeout of 2 seconds)
        # verbose=0 stops scapy from printing its own "Sent 1 packets..." messages
        reply = sr1(pkt, verbose=0, timeout=2)
        
        if reply is None:
            # No response received within the timeout window
            print(f"{ttl:2d}\t* * *\tRequest timed out.")
        elif reply.type == 11:
            # ICMP Type 11 is "Time Exceeded" (TTL expired in transit)
            print(f"{ttl:2d}\t{reply.src}")
        elif reply.type == 0:
            # ICMP Type 0 is "Echo Reply" (Destination successfully reached)
            print(f"{ttl:2d}\t{reply.src}\t(Destination Reached)")
            break
        else:
            # Catch-all for any other ICMP messages (e.g., Destination Unreachable)
            print(f"{ttl:2d}\t{reply.src}\t(Other ICMP Type: {reply.type})")
            
    print("\nTrace complete.")

if __name__ == "__main__":
    # Target can be an IP address or a hostname. 
    # Let's use Google's Public DNS as a reliable target to trace to.
    destination = "8.8.8.8" 
    manual_traceroute(destination)