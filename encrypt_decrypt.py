from hashlib import sha256
from base64 import b64decode
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


class AESCipher:
    def __init__(self, key):
        self.key = sha256(key.encode('utf8')).digest()
        print('key is')
        print(key)

    def encrypt(self, data):
        iv = get_random_bytes(AES.block_size)
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return b64encode(iv + self.cipher.encrypt(pad(data.encode('utf-8'),
                                                      AES.block_size)))

    def decrypt(self, data):
        raw = b64decode(data)
        self.cipher = AES.new(self.key, AES.MODE_CBC, raw[:AES.block_size])
        return unpad(self.cipher.decrypt(raw[AES.block_size:]), AES.block_size)

print("what happend")
# if __name__ == '__main__':
#     print('TESTING ENCRYPTION')
#     msg = input('Message...: ')
#     # pwd = input('Password..: ')
#     pwd = '0x2747d941595d43a6fc5015db1d9b6af38eeece1c4f249e01d888a9e2905707b0'
#     print('Ciphertext:', AESCipher(pwd).encrypt(msg).decode('utf-8'))
#
#     print('\nTESTING DECRYPTION')
#     cte = input('Ciphertext: ')
#     # pwd = input('Password..: ')
#     print('Message...:', AESCipher(pwd).decrypt(cte).decode('utf-8'))
# c = AESCipher(key='0x2747d941595d43a6fc501f5db1d9b6af38eeece1c4f249e01d888a9e2905707b0')
# print(encrypt(msg=msg, key='0x2747d941595d43a6fc501f5db1d9b6af38eeece1c4f249e01d888a9e2905707b0'))
# print(bytes.decode(decrypted))
# hashlib.sha256("another awesome password").digest() # => a 32 byte string
