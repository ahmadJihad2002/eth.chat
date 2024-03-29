const EthCrypto = require('eth-crypto');

const alice_privateKey='0x78982a636429ff78cd112bf675208b229d50453a2a8931d825734457e6fca9e5'
const secretMessage="ahmad"
const signature = EthCrypto.sign(
    alice_privateKey,
    EthCrypto.hash.keccak256(secretMessage)
);
const payload = {
    message: secretMessage,
    signature
};
const encrypted = await EthCrypto.encryptWithPublicKey(
    bob.publicKey, // by encrypting with bobs publicKey, only bob can decrypt the payload with his privateKey
    JSON.stringify(payload) // we have to stringify the payload before we can encrypt it
);
/*  { iv: 'c66fbc24cc7ef520a7...',
  ephemPublicKey: '048e34ce5cca0b69d4e1f5...',
  ciphertext: '27b91fe986e3ab030...',
  mac: 'dd7b78c16e462c42876745c7...'
    }
*/

// we convert the object into a smaller string-representation
const encryptedString = EthCrypto.cipher.stringify(encrypted);
// > '812ee676cf06ba72316862fd3dabe7e403c7395bda62243b7b0eea5eb..'

// now we send the encrypted string to bob over the internet.. *bieb, bieb, blob*

// we parse the string into the object again
const encryptedObject = EthCrypto.cipher.parse(encryptedString);

const decrypted = await EthCrypto.decryptWithPrivateKey(
    bob.privateKey,
    encryptedObject
);
const decryptedPayload = JSON.parse(decrypted);

// check signature
const senderAddress = EthCrypto.recover(
    decryptedPayload.signature,
    EthCrypto.hash.keccak256(decryptedPayload.message)
);

console.log(
    'Got message from ' +
    senderAddress +
    ': ' +
    decryptedPayload.message
);
// > 'Got message from 0x19C24B2d99FB91C5...: "My name is Satoshi Buterin" Buterin'