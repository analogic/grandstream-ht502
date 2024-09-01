#!/usr/bin/env python3

# Grandstream Super User by BigNerd95

import hashlib, sys, binascii

def gsresponse(password, challenge):
    key = challenge+":GrandstreamTX2013lZpRbM:"+password
    res = hashlib.md5(key.encode('ascii')).digest()[:8]
    return binascii.hexlify(res).decode("ascii")

if __name__ == "__main__":
    print("Grandstream Super User by BigNerd95\n")
    if len(sys.argv) == 3:
        password = sys.argv[1]
        challenge = sys.argv[2]
        response = gsresponse(password, challenge)
        print("Response: " + response)
    else:
        print("Usage: " + sys.argv[0] + " ADMIN_PASSWORD CHALLENGE")
        print("\nLogin via ssh in Grandstream device")
        print("Run command: gssu")
    print("")

