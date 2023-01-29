from web3 import Web3
import compile_solidity


class SmartContract:
    # get the bytecode
    byteCode = compile_solidity.byteCode
    # get the abi.json
    abi = compile_solidity.abi

    # for connecting to blockchain network
    def __init__(self, HTTP, private_key):
        # self.myAddress = "0xe0ccB13f8E54611286A68bA2433eB1c247f5b74b"
        self.HTTP = HTTP
        self.w3 = Web3(Web3.HTTPProvider(self.HTTP))
        self.is_connected = self.w3.isConnected()
        self.chainId = self.w3.eth.chainId
        self.private_key = private_key
        self.trx_index = 0
        print(self.w3.eth.gas_price)
        self.smart_contract = self.w3.eth.contract(abi=self.abi, bytecode=self.byteCode)
        # 1. build the transaction
        # 2. sign the transaction using private key
        # 3. send the transaction
        # 4. wait the Reception
        # to find the number of transaction
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
            address=Web3.toChecksumAddress('0x839867A77cFd3d147C34FC14827ef00b1910aABa'), abi=self.abi)
        # self.deploy_smart_contract = self.w3.eth.contract(
        #     address=Web3.toChecksumAddress('0xD9D59496f648450094a1AF31ca6554A830ebd745'), abi=self.abi)
        # print(self.w3.eth.getTransactionCount(self.myAddress))
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

    def create_account(self, name, sender_address, private_key, x, y):
        self.private_key = private_key
        wait_trax_receipt = self.w3.eth.wait_for_transaction_receipt(
            self.w3.eth.send_raw_transaction(
                self.w3.eth.account.sign_transaction(
                    self.deploy_smart_contract.functions.createAccount(name=name,
                                                                       sender=sender_address,
                                                                       x=str(x), y=str(y)).buildTransaction(
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

    def get_public_key_points(self, sender_address):
        return self.deploy_smart_contract.functions.get_public_key_points(userAddress=sender_address).call()
