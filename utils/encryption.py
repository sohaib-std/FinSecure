import base64

def encrypt(data):
    return base64.b64encode(data.encode()).decode()

def decrypt(encoded):
    return base64.b64decode(encoded.encode()).decode()