"""
This example is given to demonstrate an easy way to generate
RSA public and private keys to be used while creating an application
on Kuveyt Turk's API Market website, and creating signatures
before sending the requests.
"""
from Crypto.PublicKey import RSA

# Generate a key of the size 1024 bit
key = RSA.generate(1024)

# Export the private key from the rsa key.
# Private key must be stored in a secure location
# and not be shared with anyone.
privatekey = key.exportKey()
"""
e.g.
-----BEGIN RSA PRIVATE KEY-----
MIICXgIBAAKBgQC/SVnjiNTSUbqhroC/iD3uCDKGXzOoMVEuRN0v5CQVt+jROebh
ZA5uMnOHj5Yd0k3ZKQllr8AV2mZ/SH0HlkE077+QklO64eI6PtqduGZ5iJHTLnIy
VYTZDj+w6IAi5SNYqDO/ykxFN8OWv0ee0ZR9OYJ//ByE4TNSOwJXuCmvKQIDAQAB
AoGBAKuj7+qBPyYxe9vUL2ato5RQ+rUj+8Ax8HwqAqcUeWSbj2ceI5OfKmurDYtY
RgUgTgZMEkiSOTPisxIHQ1lpc7u1KwNcmp8cUCJ5hoyBR/bV2iSeKMmq77qp2STR
5XLtl8iIxEiDDmr0r1euEcF4eWrmR3yE+u/jn8WLaIgcWX25AkEA2VXt1ezUPt6Q
OIHqGAwA4qwoQc6iaGbZthIBCKKh+FD/B8QI+3sGZhZS7sX5cr3s6ME8jEiXZYvD
x5FM2an33wJBAOFREnOxeWHiMUz2Er8lhqYncaas4QeEqJx3Em24esYQxp0Lw/mh
4adYE/cxOaSMSCOcDEdNDwkqDfQxwZ3hWfcCQQDB3eDWHvgFTMshXOHQqYRwrlkK
uqQstPInc0/wwAHzW2zjJH9OtKM0lV1NGNQ3Aiw+Q4EbMfW64z2022vODcvJAkEA
1Fr7gAypcSak/nsBaiPtBtYwGD3hjJtr6qOSu9Rd6iTPfB4lozX+HiE2GAjN4hbQ
urcNH3oyDJoVMqxeZfWJOwJAec4xkzssk49t+8DnZFzwGMRWdQOgiAKZ/dTHn1OC
2XMboszsYTNEYeGKwHh34M9y2jZ/tAwcPs97LkwTh9buNQ==
-----END RSA PRIVATE KEY-----
"""
# Export the public key from the rsa key.
# This will be used while creating an application
# on API Market website.
publickey = key.publickey().exportKey()
"""
e.g.
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC/SVnjiNTSUbqhroC/iD3uCDKG
XzOoMVEuRN0v5CQVt+jROebhZA5uMnOHj5Yd0k3ZKQllr8AV2mZ/SH0HlkE077+Q
klO64eI6PtqduGZ5iJHTLnIyVYTZDj+w6IAi5SNYqDO/ykxFN8OWv0ee0ZR9OYJ/
/ByE4TNSOwJXuCmvKQIDAQAB
-----END PUBLIC KEY-----
"""