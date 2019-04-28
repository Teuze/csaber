#!/usr/bin/python
# Cipher Saber (ARCFOUR)
# Richard Jarry - 2018

from os import urandom
import argparse

def xor(a,b): # Characterwise XOR
    r = ""
    for i in range(min(len(a),len(b))):
        r = r + chr(ord(a[i]) ^ ord(b[i]))

    return r


def arc4Setup(key): 

	(A,B) = (0,0)
	state = []

	for i in range(256):
		state = state + [chr(i)]

	for K in range(256):

		B = (B + ord(key[A % len(key) % 256]) + ord(state[K % 256])) % 256

		(state[B],state[K]) = (state[K],state[B])

		A = (A + 1) % 256

	return state


def arc4GenKeyStream(state,n):

	(A,B) = (0,0)
	stream = ""

	for i in range(n):

		A = (A + 1) % 256
		B = (B + ord(state[A])) % 256
		C = (ord(state[A]) + ord(state[B])) % 256

		(state[A],state[B]) = (state[B],state[A])

		stream = stream + state[C]

	return stream

## -- Argument parsing section -- ##

parser = argparse.ArgumentParser()

parser.add_argument("-e", "--encrypt", action="store_true", help="Encrypt FILE with the CypherSaber using PASSWD.")
parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypt FILE with the CypherSaber using PASSWD.")
parser.add_argument("file", help="The file to be processed.")
parser.add_argument("passwd", help="The password to be used.")

args = parser.parse_args()
pswd = args.passwd
path = args.file

## ----------- ##

# Encryption process
if args.encrypt:

	IV = urandom(10)
	key = pswd + IV

	f = open(path,"rb")
	g = open(path+".cs1","wb")

	x = f.read()
	n = len(x)

	state  = arc4Setup(key)
	stream = arc4GenKeyStream(state,n)

	y = xor(x,stream)

	g.write(IV)
	g.write(y)

	f.close()
	g.close()

# Decryption process
elif args.decrypt:

	f = open(path,"rb")
	g = open(path+".dec","wb")

	IV = f.read(10)
	key = pswd + IV

	x = f.read()
	n = len(x)

	state  = arc4Setup(key)
	stream = arc4GenKeyStream(state,n)

	y = xor(x,stream)

	g.write(y)

	f.close()
	g.close()
