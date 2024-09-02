import random
import string

def generate_random_string(length):
    """Generate a random string of the given length."""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def encode(word):
    """Encode the word based on the given rules."""
    if len(word) < 3:
        return word[::-1]
    else:
        # Move the first letter to the end
        encoded = word[1:] + word[0]
        # Append three random characters at the start and end
        return generate_random_string(3) + encoded + generate_random_string(3)

def decode(encoded_word):
    """Decode the word based on the given rules."""
    if len(encoded_word) < 6:
        return encoded_word[::-1]
    else:
        # Remove the random characters from the start and end
        core = encoded_word[3:-3]
        # Move the last letter to the start
        return core[-1] + core[:-1]

# Example usage
if __name__ == "__main__":
    words = ['cat', 'hello', 'a', 'python', 'ok']
    
    for word in words:
        encoded = encode(word)
        decoded = decode(encoded)
        print(f"Original: {word} -> Encoded: {encoded} -> Decoded: {decoded}")
