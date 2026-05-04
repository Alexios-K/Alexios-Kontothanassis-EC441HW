# Week 10 Report: The Mechanics of Modern Encryption (SSL/TLS)

**Topic:** Security: cryptography, protocols  
**Layer:** Application  
**Type:** Report  

## 1. The Cryptographic Foundation: Asymmetric vs. Symmetric
Modern network security relies on a hybrid approach that leverages the unique strengths of two different encryption paradigms.

### A. Asymmetric Encryption (Public Key Cryptography)
Asymmetric encryption uses a mathematically linked pair of keys: a Public Key and a Private Key.
* **The Mechanism:** Data encrypted with the Public Key can only be decrypted by the corresponding Private Key.
* **The Logic:** This solves the "Key Exchange Problem." A server can openly distribute its Public Key to any client (like your browser) without fear, as the Private Key never leaves the server’s secure environment.
* **The Math:** Common algorithms like RSA or Elliptic Curve Cryptography (ECC) rely on the "trapdoor" nature of prime factorization or discrete logarithms—easy to compute in one direction, but computationally impossible to reverse without the Private Key.

### B. Symmetric Encryption (Secret Key Cryptography)
In symmetric encryption, the same key is used for both encryption and decryption.
* **The Mechanism:** Both the sender and receiver must possess the exact same secret key.
* **The Logic:** Algorithms like AES (Advanced Encryption Standard) are significantly faster and more computationally efficient than asymmetric methods.
* **The Constraint:** The challenge is getting the key to both parties securely across an unencrypted medium.

## 2. The TLS 1.3 Handshake: A Hybrid Approach
To achieve both security and speed, TLS (Transport Layer Security) uses asymmetric encryption to securely "hand over" a symmetric key.

* **Negotiation (The Client Hello):** The client sends a list of supported "Cipher Suites" and a random number (Client Random).
* **Authentication (The Server Hello):** The server sends its digital certificate and its Public Key. The client verifies the certificate against trusted Certificate Authorities (CAs) to ensure the server’s identity.
* **Key Generation (Diffie-Hellman):** Instead of simply sending a key, modern TLS 1.3 often uses Ephemeral Diffie-Hellman. Both sides contribute parameters to mathematically "derive" a shared Session Key without that key ever actually traveling across the wire.
* **Symmetric Transition:** Once the shared Session Key is derived, the "Asymmetric" phase ends. All subsequent application data (HTTP) is encrypted using high-speed Symmetric Encryption (AES).

## 3. Security Objectives Realized
By combining these methods, the protocol achieves the three pillars of the CIA Triad:

* **Confidentiality:** Eavesdroppers cannot read the data because they lack the Session Key.
* **Integrity:** Each packet includes a Message Authentication Code (MAC) or Checksum, ensuring the data hasn't been altered.
* **Authenticity:** The Digital Certificate proves you are talking to the intended server, not a "Man-in-the-Middle."