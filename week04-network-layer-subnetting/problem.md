# Artifact: IPv4 Subnetting & CIDR Problem Set

**Topic:** Network Layer (IP Addressing, CIDR, Subnetting)  
**Type:** Problem  
**Layer:** Network  

## 1. The Scenario

Imagine you are a network administrator for a new engineering lab at Boston University. You have been assigned the block 192.168.10.0/24. You need to divide this into three subnets to support different groups of devices:

* **Subnet A:** 100 workstations.
* **Subnet B:** 50 IoT sensors.
* **Subnet C:** 20 Raspberry Pi servers.

## 2. The Task

Calculate the Subnet Mask, Network Address, Usable IP Range, and Broadcast Address for each subnet using Variable Length Subnet Masking (VLSM).

## 3. Worked Solution

| Subnet | Requirement | Prefix | Subnet Mask | Network Address | Usable Range | Broadcast |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| A | 100 hosts | /25 | 255.255.255.128 | 192.168.10.0 | .1 – .126 | .127 |
| B | 50 hosts | /26 | 255.255.255.192 | 192.168.10.128 | .129 – .190 | .191 |
| C | 20 hosts | /27 | 255.255.255.224 | 192.168.10.192 | .193 – .222 | .223 |

### Logic Breakdown:

* **Subnet A:** Needs 100 hosts. The smallest power of 2 greater than 100 is $2^7=128$. This uses 7 host bits, leaving 25 bits for the network ($32-7=25$).
* **Subnet B:** Starts immediately after Subnet A's broadcast. Needs 50 hosts. $2^6=64$ is sufficient. This uses 6 host bits ($32-6=26$).
* **Subnet C:** Starts after Subnet B. Needs 20 hosts. $2^5=32$ is sufficient. This uses 5 host bits ($32-5=27$).