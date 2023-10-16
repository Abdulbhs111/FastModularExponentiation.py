def fast_modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus
    
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
        
    return result

# Example usage
base = 5
exponent = 3
modulus = 7
result = fast_modular_exponentiation(base, exponent, modulus)
print("Result:", result)
