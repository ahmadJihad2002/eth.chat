from web3 import Web3


class SmartContract:
    # get the bytecode
    byteCode = "608060405234801561001057600080fd5b506113ea806100206000396000f3fe608060405234801561001057600080fd5b506004361061007d5760003560e01c80633b9f708d1161005b5780633b9f708d14610112578063bd0f4d0d14610142578063ce43c03214610160578063de6f24bb146101905761007d565b8063133f50f514610082578063255e9c11146100b2578063298daf5b146100e2575b600080fd5b61009c60048036038101906100979190610ca7565b6101ac565b6040516100a991906110af565b60405180910390f35b6100cc60048036038101906100c79190610ca7565b610205565b6040516100d9919061108d565b60405180910390f35b6100fc60048036038101906100f79190610d34565b610378565b60405161010991906110af565b60405180910390f35b61012c60048036038101906101279190610cd4565b610469565b60405161013991906110af565b60405180910390f35b61014a610599565b604051610157919061106b565b60405180910390f35b61017a60048036038101906101759190610ca7565b61071f565b60405161018791906110ca565b60405180910390f35b6101aa60048036038101906101a59190610cd4565b61083a565b005b6000806000808473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060000180546101fb90611266565b9050119050919050565b606060006102133384610975565b905060016000828152602001908152602001600020805480602002602001604051908101604052809291908181526020016000905b8282101561036c57838290600052602060002090600302016040518060600160405290816000820160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001600182015481526020016002820180546102db90611266565b80601f016020809104026020016040519081016040528092919081815260200182805461030790611266565b80156103545780601f1061032957610100808354040283529160200191610354565b820191906000526020600020905b81548152906001019060200180831161033757829003601f168201915b50505050508152505081526020019060010190610248565b50505050915050919050565b6000801515610386336101ac565b1515146103c8576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016103bf9061110c565b60405180910390fd5b6000838390501161040e576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016104059061112c565b60405180910390fd5b82826000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600001919061045e929190610b13565b506001905092915050565b60006104ba338585858080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f82011690508083019250505050505050610a0d565b61058e84336000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600001805461050b90611266565b80601f016020809104026020016040519081016040528092919081815260200182805461053790611266565b80156105845780601f1061055957610100808354040283529160200191610584565b820191906000526020600020905b81548152906001019060200180831161056757829003601f168201915b5050505050610a0d565b600190509392505050565b60606000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600101805480602002602001604051908101604052809291908181526020016000905b8282101561071657838290600052602060002090600202016040518060400160405290816000820160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200160018201805461068590611266565b80601f01602080910402602001604051908101604052809291908181526020018280546106b190611266565b80156106fe5780601f106106d3576101008083540402835291602001916106fe565b820191906000526020600020905b8154815290600101906020018083116106e157829003601f168201915b505050505081525050815260200190600101906105fc565b50505050905090565b606061072a826101ac565b610769576040517f08c379a0000000000000000000000000000000000000000000000000000000008152600401610760906110ec565b60405180910390fd5b6000808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060000180546107b590611266565b80601f01602080910402602001604051908101604052809291908181526020018280546107e190611266565b801561082e5780601f106108035761010080835404028352916020019161082e565b820191906000526020600020905b81548152906001019060200180831161081157829003601f168201915b50505050509050919050565b60006108463385610975565b9050600060405180606001604052803373ffffffffffffffffffffffffffffffffffffffff16815260200142815260200185858080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f8201169050808301925050505050505081525090506001600083815260200190815260200160002081908060018154018082558091505060019003906000526020600020906003020160009091909190915060008201518160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060208201518160010155604082015181600201908051906020019061096b929190610b99565b5050505050505050565b60008173ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff1610156109db5782826040516020016109be92919061103f565b604051602081830303815290604052805190602001209050610a07565b81836040516020016109ee92919061103f565b6040516020818303038152906040528051906020012090505b92915050565b600060405180604001604052808473ffffffffffffffffffffffffffffffffffffffff1681526020018381525090506000808573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060010181908060018154018082558091505060019003906000526020600020906002020160009091909190915060008201518160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506020820151816001019080519060200190610b0a929190610b99565b50505050505050565b828054610b1f90611266565b90600052602060002090601f016020900481019282610b415760008555610b88565b82601f10610b5a57803560ff1916838001178555610b88565b82800160010185558215610b88579182015b82811115610b87578235825591602001919060010190610b6c565b5b509050610b959190610c1f565b5090565b828054610ba590611266565b90600052602060002090601f016020900481019282610bc75760008555610c0e565b82601f10610be057805160ff1916838001178555610c0e565b82800160010185558215610c0e579182015b82811115610c0d578251825591602001919060010190610bf2565b5b509050610c1b9190610c1f565b5090565b5b80821115610c38576000816000905550600101610c20565b5090565b600081359050610c4b8161139d565b92915050565b60008083601f840112610c6757610c666112f0565b5b8235905067ffffffffffffffff811115610c8457610c836112eb565b5b602083019150836001820283011115610ca057610c9f6112f5565b5b9250929050565b600060208284031215610cbd57610cbc6112ff565b5b6000610ccb84828501610c3c565b91505092915050565b600080600060408486031215610ced57610cec6112ff565b5b6000610cfb86828701610c3c565b935050602084013567ffffffffffffffff811115610d1c57610d1b6112fa565b5b610d2886828701610c51565b92509250509250925092565b60008060208385031215610d4b57610d4a6112ff565b5b600083013567ffffffffffffffff811115610d6957610d686112fa565b5b610d7585828601610c51565b92509250509250929050565b6000610d8d8383610fa3565b905092915050565b6000610da18383610fe0565b905092915050565b610db2816111eb565b82525050565b610dc9610dc4826111eb565b611298565b82525050565b6000610dda8261116c565b610de481856111a7565b935083602082028501610df68561114c565b8060005b85811015610e325784840389528151610e138582610d81565b9450610e1e8361118d565b925060208a01995050600181019050610dfa565b50829750879550505050505092915050565b6000610e4f82611177565b610e5981856111b8565b935083602082028501610e6b8561115c565b8060005b85811015610ea75784840389528151610e888582610d95565b9450610e938361119a565b925060208a01995050600181019050610e6f565b50829750879550505050505092915050565b610ec2816111fd565b82525050565b6000610ed382611182565b610edd81856111c9565b9350610eed818560208601611233565b610ef681611304565b840191505092915050565b6000610f0c82611182565b610f1681856111da565b9350610f26818560208601611233565b610f2f81611304565b840191505092915050565b6000610f476017836111da565b9150610f5282611322565b602082019050919050565b6000610f6a6014836111da565b9150610f758261134b565b602082019050919050565b6000610f8d6019836111da565b9150610f9882611374565b602082019050919050565b6000604083016000830151610fbb6000860182610da9565b5060208301518482036020860152610fd38282610ec8565b9150508091505092915050565b6000606083016000830151610ff86000860182610da9565b50602083015161100b6020860182611030565b50604083015184820360408601526110238282610ec8565b9150508091505092915050565b61103981611229565b82525050565b600061104b8285610db8565b60148201915061105b8284610db8565b6014820191508190509392505050565b600060208201905081810360008301526110858184610dcf565b905092915050565b600060208201905081810360008301526110a78184610e44565b905092915050565b60006020820190506110c46000830184610eb9565b92915050565b600060208201905081810360008301526110e48184610f01565b905092915050565b6000602082019050818103600083015261110581610f3a565b9050919050565b6000602082019050818103600083015261112581610f5d565b9050919050565b6000602082019050818103600083015261114581610f80565b9050919050565b6000819050602082019050919050565b6000819050602082019050919050565b600081519050919050565b600081519050919050565b600081519050919050565b6000602082019050919050565b6000602082019050919050565b600082825260208201905092915050565b600082825260208201905092915050565b600082825260208201905092915050565b600082825260208201905092915050565b60006111f682611209565b9050919050565b60008115159050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b60005b83811015611251578082015181840152602081019050611236565b83811115611260576000848401525b50505050565b6000600282049050600182168061127e57607f821691505b60208210811415611292576112916112bc565b5b50919050565b60006112a3826112aa565b9050919050565b60006112b582611315565b9050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b600080fd5b600080fd5b600080fd5b600080fd5b600080fd5b6000601f19601f8301169050919050565b60008160601b9050919050565b7f55736572206973206e6f74207265676973746572656421000000000000000000600082015250565b7f5573657220616c72656164792065786973747321000000000000000000000000600082015250565b7f557365726e616d652063616e6e6f7420626520656d7074792100000000000000600082015250565b6113a6816111eb565b81146113b157600080fd5b5056fea264697066735822122071f22b6f9b0fb4199eb2a383fd1f3df926e0e34388cffdb7a09ac9863093336264736f6c63430008070033"
    # get the abi
    abi = [
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "friendAddress",
                    "type": "address"
                },
                {
                    "internalType": "string",
                    "name": "name",
                    "type": "string"
                }
            ],
            "name": "addFriend",
            "outputs": [
                {
                    "internalType": "bool",
                    "name": "",
                    "type": "bool"
                }
            ],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "pubkey",
                    "type": "address"
                }
            ],
            "name": "checkUserExists",
            "outputs": [
                {
                    "internalType": "bool",
                    "name": "",
                    "type": "bool"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "string",
                    "name": "name",
                    "type": "string"
                }
            ],
            "name": "createAccount",
            "outputs": [
                {
                    "internalType": "bool",
                    "name": "",
                    "type": "bool"
                }
            ],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "getMyFriendList",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "address",
                            "name": "pubkey",
                            "type": "address"
                        },
                        {
                            "internalType": "string",
                            "name": "name",
                            "type": "string"
                        }
                    ],
                    "internalType": "struct chat.friend[]",
                    "name": "",
                    "type": "tuple[]"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "pubkey",
                    "type": "address"
                }
            ],
            "name": "getUsername",
            "outputs": [
                {
                    "internalType": "string",
                    "name": "",
                    "type": "string"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "friend_key",
                    "type": "address"
                }
            ],
            "name": "readMessage",
            "outputs": [
                {
                    "components": [
                        {
                            "internalType": "address",
                            "name": "sender",
                            "type": "address"
                        },
                        {
                            "internalType": "uint256",
                            "name": "timestamp",
                            "type": "uint256"
                        },
                        {
                            "internalType": "string",
                            "name": "msg",
                            "type": "string"
                        }
                    ],
                    "internalType": "struct chat.message[]",
                    "name": "",
                    "type": "tuple[]"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "friend_key",
                    "type": "address"
                },
                {
                    "internalType": "string",
                    "name": "_msg",
                    "type": "string"
                }
            ],
            "name": "sendMessage",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        }
    ]

    # for connecting to blockchain
    def __init__(self, HTTP, chainId, privateKey, publicKey, name):
        self.HTTP = HTTP

        self.w3 = Web3(Web3.HTTPProvider(self.HTTP))
        self.chainId = chainId
        #
        # self.chainId = self.w3.eth.chainId
        self.name = name
        self.myAddress = publicKey
        self.privateKey = privateKey
        # to create the contract in python
        self.nonce = self.w3.eth.getTransactionCount(self.myAddress)
        print(self.nonce)
        self.smart_contract = self.w3.eth.contract(abi=self.abi, bytecode=self.byteCode)
        # 1. build the transaction
        # 2. sign the transaction using private key
        # 3. send the transaction
        # 4. wait the Reception
        # to find the number of transaction
        print(self.w3.eth.getTransactionCount(self.myAddress))

        # 1.
        self.myAddress = publicKey
        self.privateKey = privateKey
        print(" sitting up the transaction ... ")
        transaction = self.smart_contract.constructor().build_transaction(
            {"gasPrice": self.w3.eth.gas_price, "chainId": self.chainId, "from": self.myAddress,
             "nonce": self.nonce})
        print("done !")
        print(self.w3.eth.getTransactionCount(self.myAddress))
        # 2.
        print("sign the transaction...")
        sign = self.w3.eth.account.sign_transaction(transaction, self.privateKey)
        print("done")
        print(self.w3.eth.getTransactionCount(self.myAddress))
        # 3.
        print("sending the transaction... ")
        signedTransaction = self.w3.eth.sendRawTransaction(sign.rawTransaction)
        print("done")
        print(self.w3.eth.getTransactionCount(self.myAddress))
        # waiting the transaction to go throw
        print("waiting the reception... ")
        waitRecept = self.w3.eth.wait_for_transaction_receipt(signedTransaction)
        print("done")
        print(self.w3.eth.getTransactionCount(self.myAddress))
        self.deploy_smart_contract = self.w3.eth.contract(address=waitRecept.contractAddress, abi=self.abi)
        print("contract been deployed ")
        print(self.w3.eth.getTransactionCount(self.myAddress))
        wait_trax_receipt = self.w3.eth.wait_for_transaction_receipt(
            self.w3.eth.send_raw_transaction(
                self.w3.eth.account.sign_transaction(
                    self.deploy_smart_contract.functions.createAccount(name=self.name).buildTransaction({
                        "gasPrice": self.w3.eth.gas_price, "chainId": self.chainId, "from": self.myAddress,
                        "nonce": self.nonce + 1
                    }), self.privateKey).rawTransaction))

        print(wait_trax_receipt)

    def addFriend(self, friendName, friendAddress):
        wait_trax_receipt = self.w3.eth.wait_for_transaction_receipt(
            self.w3.eth.send_raw_transaction(
                self.w3.eth.account.sign_transaction(
                    self.deploy_smart_contract.functions.addFriend(friendAddress=friendAddress,
                                                                   name=friendName).buildTransaction({
                        "gasPrice": self.w3.eth.gas_price, "chainId": self.chainId, "from": self.myAddress,
                        "nonce": self.w3.eth.getTransactionCount(self.myAddress)
                    }), self.privateKey).rawTransaction))

        return wait_trax_receipt

    def sendMessage(self, msg, receiverAddress):
        wait_trax_receipt = self.w3.eth.wait_for_transaction_receipt(
            self.w3.eth.send_raw_transaction(
                self.w3.eth.account.sign_transaction(
                    self.deploy_smart_contract.functions.sendMessage(friend_key=receiverAddress,
                                                                     _msg=msg).buildTransaction({
                        "gasPrice": self.w3.eth.gas_price, "chainId": self.chainId, "from": self.myAddress,
                        "nonce": self.w3.eth.getTransactionCount(self.myAddress)
                    }), self.privateKey).rawTransaction))

    def readMessages(self, friendAddress):
        return self.deploy_smart_contract.functions.readMessage(friendAddress).call()

    def checkUserExists(self, Address):
        return self.deploy_smart_contract.functions.checkUserExists(Address).call()

    def showfriendList(self):
        return self.deploy_smart_contract.functions.getMyFriendList().call()

#
# c = SmartContract(HTTP="https://sepolia.infura.io/v3/0dc1865d3cb84781999f5781077d8ddb", chainId=1,
#                   publicKey="0xe0ccB13f8E54611286A68bA2433eB1c247f5b74b",
#                   privateKey="0x78982a636429ff78cd112bf675208b229d50453a2a8931d825734457e6fca9e5",
#                   name="ahmad")

# print(c.nonce)
# print(c.addFriend(friendName="laith", friendAddress="0x54F08CBFF5E3E71BA0D7f4248af2c8D519B8958D"))
# c.sendMessage(msg="hay hay maan", receiverAddress="0x54F08CBFF5E3E71BA0D7f4248af2c8D519B8958D")
# c.sendMessage(msg="hay hay ", receiverAddress="0x54F08CBFF5E3E71BA0D7f4248af2c8D519B8958D")
# c.sendMessage(msg="yo yo yo ", receiverAddress="0x54F08CBFF5E3E71BA0D7f4248af2c8D519B8958D")
# c.sendMessage(msg="yo yo yo ", receiverAddress="0x54F08CBFF5E3E71BA0D7f4248af2c8D519B8958D")
# c.sendMessage(msg="how you doing ", receiverAddress="0x54F08CBFF5E3E71BA0D7f4248af2c8D519B8958D")
# print(c.checkUserExists("0x54F08CBFF5E3E71BA0D7f4248af2c8D519B8958D"))
#
# for i in range(5):
#     print(c.readMessages(friendAddress="0x54F08CBFF5E3E71BA0D7f4248af2c8D519B8958D")[i][2])
# now we can call the function from the smart contract. We can call it using two keywords
# call :simulate the call and get return value but not changing the state
# transaction : calling the function and changing the state of the network
