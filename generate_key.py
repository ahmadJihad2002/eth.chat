from eth_keys import keys
from eth_utils import decode_hex
from tinyec import registry


# priv_key_bytes = decode_hex('0x78982a636429ff78cd112bf675208b229d50453a2a8931d825734457e6fca9e5')
# priv_key = keys.PrivateKey(priv_key_bytes)
# pub_key = priv_key.public_key
# print(pub_key)
# print(pub_key.to_checksum_address())
#
# curve = registry.get_curve('brainpoolP256r1')
#
#
# def compress_point(point):
#     return hex(point.x) + hex(point.y % 2)[2:]
#
#
# def get_public_key(private_key):
#     pubKey = private_key * curve.g
#
#     print("pub mm mlic key:", compress_point(pubKey))
#     # priv_key_bytes = decode_hex(private_key)
#     # priv_key = keys.PrivateKey(priv_key_bytes)
#     # pub_key = priv_key.public_key
#     # print(pub_key)
#     # print(pub_key.to_checksum_address())
#
#
# get_public_key(private_key=int(0x78982a636429ff78cd112bf675208b229d50453a2a8931d825734457e6fca9e5))


def generate_key(public_key, my_private_key):
    print(type(public_key))
    sharedECCKey = public_key * my_private_key
    return sharedECCKey


# def ecc_calc_decryption_key(privKey, ciphertextPubKey):
#     sharedECCKey = ciphertextPubKey * privKey
#     return sharedECCKey

#
# def derive_key_using_public_key(public_key):
#     (encryptKey, ciphertextPubKey) = ecc_calc_encryption_keys(public_key)
#     print("ciphertext pubKey:", compress_point(ciphertextPubKey))
#     print("encryption key:", compress_point(encryptKey))
#     return compress_point(encryptKey)
#
#
# def derive_key_using_private_key(private_key):
#     decryptKey = ecc_calc_decryption_key(private_key, ciphertextPubKey)
#     print("decryption key:", compress_point(decryptKey))
#

# def get_my_public_key(privKey):
#     pubKey = privKey * curve.g
#     return compress_point(pubKey)
#

# privKey = secrets.randbelow(curve.field.n)
# privKey = int('0x78982a636429ff78cd112bf675208b229d50453a2a8931d825734457e6fca9e5', 16)
# public_key = int('0xe0ccB13f8E54611286A68bA2433eB1c247f5b74b', 16)
# privKey2 = int('0x35343465e7e5924efae2ac12fb00d9e3ce5d52657603593690b6e724cbedd186', 16)
# public_key2 = int('0xf579A42a3dAa4284b8A5A8C0B4012A81BB2005a7', 16)
# pubKey = privKey * curve.g
# print("private key:", hex(privKey))
# print("public key:", compress_point(pubKey))
#
# encryptKey = generate_key(his_public_key, privKey)
# print("encryption key:", encryptKey)
# an_integer = int(hex_string, 16)
#
# hex_value = hex(an_integer)
# Key = generate_key(public_key2, privKey)
# print(" the key ", Key)
# Key2 = generate_key(public_key, privKey2)
# print(" the key2 ", Key)
# Key3 = generate_key(public_key, int('35343465e7e5924efee2ac82fb00d9e3c85d52657603593690b6e724cbedd186',16))
# print(" the key2 ", Key3)
