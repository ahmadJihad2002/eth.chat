from solcx import compile_standard, install_solc
import json

with open("smartContract.sol", "r") as file:
    smartContract: str = file.read()
install_solc("0.8.8")
compiled_solidity = compile_standard(
    {
        "language": "Solidity",
        "sources": {"/contracts/smartContract.sol": {"content": smartContract}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            },
        },
    },
    solc_version="0.8.8",
)
with open("compiledContract.json", "w") as jsonFile:
    json.dump(compiled_solidity, jsonFile)

byteCode = compiled_solidity["contracts"]["/contracts/smartContract.sol"]["chat"]["evm"]["bytecode"]["object"]

abi = compiled_solidity["contracts"]["/contracts/smartContract.sol"]["chat"]["abi"]
