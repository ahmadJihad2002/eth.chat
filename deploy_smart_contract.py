from web3 import Web3
import compile_solidity


class SmartContract:
    # get the bytecode
    byteCode = compile_solidity.byteCode
    # get the abi.json
    abi = compile_solidity.abi

    # for connecting to blockchain network
    def __init__(self, HTTP):
        self.myAddress = "0xe0ccB13f8E54611286A68bA2433eB1c247f5b74b"
        self.HTTP = HTTP
        self.w3 = Web3(Web3.HTTPProvider(self.HTTP))
        self.is_connected = self.w3.isConnected()
        self.chainId = self.w3.eth.chainId
        self.private_key = '0x78982a636429ff78cd112bf675208b229d50453a2a8931d825734457e6fca9e5'
        self.trx_index = 0
        # print(self.w3.eth.gas_price)
        # self.smart_contract = self.w3.eth.contract(abi=self.abi, bytecode=self.byteCode)
        # # 1. build the transaction
        # # 2. sign the transaction using private key
        # # 3. send the transaction
        # # 4. wait the Reception
        # # to find the number of transaction
        # self.nonce = self.w3.eth.getTransactionCount(self.myAddress)
        #
        # print(" sitting up the transaction ... ")
        # transaction = self.smart_contract.constructor().build_transaction(
        #     {"gasPrice": self.w3.eth.gas_price, "chainId": self.chainId, "from": self.myAddress,
        #      "nonce": self.nonce + self.trx_index})
        # self.trx_index += 1
        # print("done !")
        # print(self.w3.eth.getTransactionCount(self.myAddress))
        # # 2.
        # print("sign the transaction...")
        # sign = self.w3.eth.account.sign_transaction(transaction, self.private_key)
        # print("done")
        # print(self.w3.eth.getTransactionCount(self.myAddress))
        # # 3.
        # print("sending the transaction... ")
        # signedTransaction = self.w3.eth.sendRawTransaction(sign.rawTransaction)
        # print("done")
        # print(self.w3.eth.getTransactionCount(self.myAddress))
        # # waiting the transaction to go throw
        # print("waiting the reception... ")
        # waitRecept = self.w3.eth.wait_for_transaction_receipt(signedTransaction)
        # print("done")
        # print(self.w3.eth.getTransactionCount(self.myAddress))
        # self.deploy_smart_contract = self.w3.eth.contract(address=waitRecept.contractAddress, abi=self.abi)
        # print(waitRecept.contractAddress)

        self.deploy_smart_contract = self.w3.eth.contract(
            address=Web3.toChecksumAddress('0x6551C5FD37a6B4Bf0c542A5f83C0B2a1765754eA'), abi=self.abi)
        print(self.w3.eth.getTransactionCount(self.myAddress))
        print("contract been deployed ")

    def addFriend(self, friendName, friendAddress, sender_address):
        print(self.w3.eth.get_balance(Web3.toChecksumAddress('0xe0ccB13f8E54611286A68bA2433eB1c247f5b74b')))
        wait_trax_receipt = self.w3.eth.wait_for_transaction_receipt(
            self.w3.eth.send_raw_transaction(
                self.w3.eth.account.sign_transaction(
                    self.deploy_smart_contract.functions.addFriend(friendAddress=friendAddress,
                                                                   name=friendName,
                                                                   sender=sender_address).buildTransaction({
                        "gasPrice": self.w3.eth.gas_price, "chainId": self.chainId, "from": sender_address,
                        "nonce": self.w3.eth.getTransactionCount(sender_address) + self.trx_index
                    }), self.private_key).rawTransaction))
        self.trx_index += 1
        print('data for adding friend ')
        print(wait_trax_receipt)
        print(self.w3.eth.get_balance(Web3.toChecksumAddress('0xe0ccB13f8E54611286A68bA2433eB1c247f5b74b')))

    def create_account(self, name, sender_address, private_key):
        self.private_key = private_key
        wait_trax_receipt = self.w3.eth.wait_for_transaction_receipt(
            self.w3.eth.send_raw_transaction(
                self.w3.eth.account.sign_transaction(
                    self.deploy_smart_contract.functions.createAccount(name=name,
                                                                       sender=sender_address,
                                                                        ).buildTransaction(
                        {
                            "gasPrice": self.w3.eth.gas_price, "chainId": self.chainId, "from": sender_address,
                            "nonce": self.w3.eth.getTransactionCount(sender_address) + self.trx_index

                        }), self.private_key).rawTransaction))
        self.trx_index += 1
        print(wait_trax_receipt)

        return wait_trax_receipt

    def sendMessage(self, msg, receiverAddress, sender_address):
        wait_trax_receipt = self.w3.eth.wait_for_transaction_receipt(
            self.w3.eth.send_raw_transaction(
                self.w3.eth.account.sign_transaction(
                    self.deploy_smart_contract.functions.sendMessage(friend_key=receiverAddress,
                                                                     _msg=msg, sender=sender_address).buildTransaction({
                        "gasPrice": self.w3.eth.gas_price, "chainId": self.chainId, "from": sender_address,
                        "nonce": self.w3.eth.getTransactionCount(sender_address) + self.trx_index,
                    }), self.private_key).rawTransaction))
        self.trx_index += 1
        print(wait_trax_receipt)

    def readMessages(self, friendAddress, sender_address):
        return self.deploy_smart_contract.functions.readMessage(friendAddress, sender=sender_address).call()

    def checkUserExists(self, Address):
        return self.deploy_smart_contract.functions.checkUserExists(Address).call()

    def showfriendList(self, sender_address):
        return self.deploy_smart_contract.functions.getMyFriendList(sender=sender_address).call()

    # def get_user_public_key(self, sender_address):
    #     return self.deploy_smart_contract.functions.get_user_public_key(sender_address).call()


# c = SmartContract(
#     HTTP='https://serene-wider-slug.ethereum-goerli.discover.quiknode.pro/e7ea9294e3c8a1396ce7175a378d32aa42d9cb31/')

"""
# c = SmartContract(HTTP="HTTP://127.0.0.1:7545", chainId=1337,
#                   publicKey="0x99cfc386DeF98a826f6b3473D56A952bd37e55D8",
#                   privateKey="0x7eb2c59d6253100b18c494c5023fd3186a555d3a1c2372201d72a48cba708655",
#                   name="ahmad")
# c = SmartContract(HTTP="https://serene-wider-slug.ethereum-goerli.discover.quiknode.pro/e7ea9294e3c8a1396ce7175a378d32aa42d9cb31/", chainId=1,
#                   publicKey="0xe0ccB13f8E54611286A68bA2433eB1c247f5b74b",
#                   privateKey="0x78982a636429ff78cd112bf675208b229d50453a2a8931d825734457e6fca9e5",
#                   name="ahmad")
print("creating account")
# c.create_account("ahmad", sender_address="0xe0ccB13f8E54611286A68bA2433eB1c247f5b74b")
print("done")
print("adding friend ...")
print(c.checkUserExists('0xe0ccB13f8E54611286A68bA2433eB1c247f5b74b'))
# print(c.checkUserExists("0xB2231D23966305D1B9010025d27bB078CC747bff"))
# c.sendMessage(msg="yo yo yo it's ahmad jihad :)", receiverAddress="0xB2231D23966305D1B9010025d27bB078CC747bff",
#               sender_address="0xe0ccB13f8E54611286A68bA2433eB1c247f5b74b")
# print("adding friend ")
# c.addFriend(friendAddress='0xB2231D23966305D1B9010025d27bB078CC747bff', friendName="laith",
#             sender_address="0xe0ccB13f8E54611286A68bA2433eB1c247f5b74b")
# print("friend been added ")
# print(c.readMessages(friendAddress="0xB2231D23966305D1B9010025d27bB078CC747bff",
#                      sender_address="0xe0ccB13f8E54611286A68bA2433eB1c247f5b74b"))
#     print("friend is not reg yet ")
#     print("friend made the reg ")
#     print("friend been added")
#     print("send the message")
#     c.sendMessage(msg="yo yo yo it's ahmad jihad :)", receiverAddress="0xB2231D23966305D1B9010025d27bB078CC747bff")
#     print(c.readMessages(friendAddress="0xB2231D23966305D1B9010025d27bB078CC747bff"))
# print("my friend list ")
d = c.showfriendList(sender_address="0xe0ccB13f8E54611286A68bA2433eB1c247f5b74b")
print(d)
print("done")
# now we can call the function from the smart contract. We can call it using two keywords
# call :simulate the call and get return value but not changing the state
# transaction : calling the function and changing the state of the network
"""
