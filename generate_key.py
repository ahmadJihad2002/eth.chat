from eth_keys import keys
from eth_utils import decode_hex
from tinyec import registry

# priv_key_bytes = decode_hex('0x78982a636429ff78cd112bf675208b229d50453a2a8931d825734457e6fca9e5')
# priv_key = keys.PrivateKey(priv_key_bytes)
# pub_key = priv_key.public_key
# print(pub_key)
# print(pub_key.to_checksum_address())
#
curve = registry.get_curve('brainpoolP256r1')


#
def compress_point(point):
    return hex(point.x) + hex(point.y % 2)[2:]


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
    print('sharedECCKey')
    print(sharedECCKey)
    return sharedECCKey


# # pri = '0x78982a636429ff78cd112bf675208b229d50453a2a8931d825734457e6fca9e5'
# # pri1 = '0x56ebf286fa42b79ccbfa8c7f80ad43dd6ce8a901e3a3003bebd6e157aa4d6624'
# #
# pubKey = int(pri, 16) * curve.g
# pubKey1 = int(pri1, 16) * curve.g
# print("public key ")
# print(pubKey)
# print("public key1 ")
# print(pubKey1)
# Key = generate_key(pubKey, int(pri1, 16))
# print(" the key ", compress_point(Key))
# Key2 = generate_key(pubKey1, int(pri, 16))
# print(" the key2 ", compress_point(Key2))
