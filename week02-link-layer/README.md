# Week 2: Link Layer & Error Control

**Topic:** Link layer (frames, error control, CRC)
**Type:** Lab
**Description:** 
This lab explores error control in the link layer by implementing a Cyclic Redundancy Check (CRC) calculator in Python. The script (`crc_calculator.py`) converts string messages into binary data, calculates the CRC remainder using modulo-2 division, appends it to form a codeword, and then verifies the codeword on the simulated "receiver" side to demonstrate error detection.

### Usage
Run `python crc_calculator.py` in the terminal to see a demonstration of CRC encoding and error detection.