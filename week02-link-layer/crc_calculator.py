def xor(a, b):
    """Perform XOR operation on two binary strings of the same length."""
    result = []
    # We start from 1 because the first bit of the XOR in modulo-2 division is always 0
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(dividend, divisor):
    """Perform modulo-2 division (CRC division)."""
    pick = len(divisor)
    tmp = dividend[0:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            # If the leading bit is 1, XOR with the divisor
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            # If the leading bit is 0, XOR with all zeros
            tmp = xor('0' * pick, tmp) + dividend[pick]
        pick += 1

    # For the last step
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    return tmp

def encode_data(data_string, polynomial):
    """Encode a string by calculating and appending the CRC remainder."""
    # Convert string to a single binary string
    binary_data = ''.join(format(ord(c), '08b') for c in data_string)
    
    # Append zeros (length of polynomial - 1)
    appended_data = binary_data + '0' * (len(polynomial) - 1)
    
    # Calculate remainder
    remainder = mod2div(appended_data, polynomial)
    
    # Append remainder to the original binary data to create the codeword
    codeword = binary_data + remainder
    return binary_data, codeword, remainder

def check_data(codeword, polynomial):
    """Check if the received codeword has errors."""
    remainder = mod2div(codeword, polynomial)
    # If remainder is all zeros, no error was detected
    if '1' not in remainder:
        return True, remainder
    else:
        return False, remainder

if __name__ == '__main__':
    # Example message and a CRC-8 generator polynomial (x^8 + x^2 + x + 1 -> 100000111)
    message = "EC441"
    generator = "100000111"
    
    print("--- SENDER SIDE ---")
    print(f"Original Message: '{message}'")
    print(f"Generator Polynomial: {generator}")
    
    binary_data, codeword, remainder = encode_data(message, generator)
    print(f"Binary Data: {binary_data}")
    print(f"CRC Remainder: {remainder}")
    print(f"Transmitted Codeword: {codeword}\n")
    
    print("--- RECEIVER SIDE (NO ERROR) ---")
    is_valid, check_rem = check_data(codeword, generator)
    print(f"Received Codeword: {codeword}")
    print(f"Receiver Remainder: {check_rem}")
    print(f"Data Intact? {is_valid}\n")

    print("--- RECEIVER SIDE (WITH 1-BIT ERROR) ---")
    # Introduce a 1-bit error by flipping the last bit
    error_codeword = codeword[:-1] + ('1' if codeword[-1] == '0' else '0')
    is_valid_err, err_rem = check_data(error_codeword, generator)
    print(f"Received Codeword: {error_codeword}")
    print(f"Receiver Remainder: {err_rem}")
    print(f"Data Intact? {is_valid_err}")