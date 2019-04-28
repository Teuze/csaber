# Cipher Saber

A ancient Jedi tool for basic ARCFOUR encryption.

**Warning** : This is so outdated it should only be used as a last resort encryption method.
The only advantage of this method is its simplicity of use and application by a human being.
It may prove itself useful when time comes for the rise of the machines.

## Usage

```bash
# Use interactive & non-persistent variables
# to avoid keeping your plaintext password
# in your history and environment !

read -s $PASS

# File encryption
./csaber -e file.txt $PASS

# File decryption
./csaber -d file.cs $PASS

unset PASS
```

## Cryptographic Overview

CipherSaber relies on ARCFOUR, an open-source implementation of RC4 by Ronald Rivest.
It generates a pseudorandom stream of bits from a key and an initialization vector (IV).
This pseudorandom stream is then bitwise-XOR'ed to the file to encrypt, mimicking that way
the one-time-pad method (which is Shannon-secure).

The stream is generated using a permutation table (called `state` in my code)
and two index variables `A` and `B`. It is a two-step process.

1. **Key Scheduling** : Initializes the permutation table using key+IV.
2. **Pseudo-Random Stream Generation** : Generates the pseudorandom stream
    by iterating on the the table state.

## Links

[The Cyphersaber Page](http://ciphersaber.gurus.org/) <br/>
[Wikipedia -- ARCFOUR](https://en.wikipedia.org/wiki/ARCFOUR)
