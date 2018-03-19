#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#%reset -f

alphabet = "abcdefghijklmnopqrstuvwxyz"

#Encryption Procedure

plainText = input("Enter the plain text : ").lower().replace(" ","")
key = input("Enter the key : ").lower().replace(" ","")
#preparing keystream
keystream = ""
for i in range(len(plainText)):
    keystream += key[i%len(key)]
cipherText = ""
for i in range(len(plainText)):
    cipherText += alphabet[(alphabet.index(keystream[i])+alphabet.index(plainText[i]))%26]
print(cipherText)

#Decryption Procedure

cipherText = input("Enter the cipher text : ").lower().replace(" ","")
key = input("Enter the key : ").lower().replace(" ","")
#preparing keystream
keystream = ""
for i in range(len(cipherText)):
    keystream += key[i%len(key)]
plainText = ""
for i in range(len(cipherText)):
    plainText += alphabet[(alphabet.index(cipherText[i])-alphabet.index(keystream[i]))%26]
print(plainText)