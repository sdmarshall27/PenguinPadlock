from cryptography.fernet import Fernet


def gen_key():
    # if we decide to advance our security we can generate more keys.
    key = Fernet.generate_key()
    return key
    # write key into whatever we want

def load_key():
    # open up key from wherever it is stored.
    key = b'02KfbsBZfQvBBcHP5u-msoF0jqotlGwd9zReXFOq53Y='

    return key


def encrypt(message):
    key = load_key()
    encodedMessage = message.encode()
    f = Fernet(key)
    encryptedMessage = f.encrypt(encodedMessage)
    return encryptedMessage


def decrypt(encryptedMessage):
    key = load_key()
    f = Fernet(key)
    decryptedMessage = f.decrypt(encryptedMessage)
    return decryptedMessage




