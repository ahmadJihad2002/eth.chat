import tinyec.ec
from eth_keys import keys
from eth_utils import decode_hex
# from tinyec import registry
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


pubKey = int('0x78982a636429ff78cd112bf675208b229d50453a2a8931d825734457e6fca9e5', 16) * curve.g
print(pubKey)


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
    print("i am in genrate point ")
    print(public_key)
    print(type(public_key))

    d = tinyec.ec.Point(x=int(public_key[0]), y=int(public_key[1]), curve=curve)
    print(d)

    sharedECCKey = d * my_private_key
    # sharedECCKey = public_key * my_private_key

    print('sharedECCKey')
    print(compress_point(sharedECCKey))
    return compress_point(sharedECCKey)


def get_x_y(private_key):
    pub_key_points = private_key * curve.g

    return pub_key_points.x, pub_key_points.y

#
# private_key = '0x78982a636429ff78cd112bf675208b229d50453a2a8931d825734457e6fca9e5'
# print(get_x_y(int(private_key, 16))[0])
# print(get_x_y(int(private_key, 16))[1])
#
# generate_key(("54581745882493735518927915598045440997261088096230584616563249481911156321287",
#               "58678824917114178418404419944743326857203516751209767386125368317488001630745"),
#              int('0x78982a636429ff78cd112bf675208b229d50453a2a8931d825734457e6fca9e5', 16))
# get_x_y(0x78982a636429ff78cd112bf675208b229d50453a2a8931d825734457e6fca9e5)
# print(get_x_y(0x78982a636429ff78cd112bf675208b229d50453a2a8931d825734457e6fca9e5)[0])
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
