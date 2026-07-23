import base64

c = base64.b64decode("EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0/GBlgaVVIJDURDSQ1VRY=")

key = [ord(p) ^ b for p, b in zip('{"showpassword":"no","bgcolor":"#ffffff"}', c)][:4]
new = '{"showpassword":"yes","bgcolor":"#ffffff"}'
out = bytes(ord(new[i]) ^ key[i % 4] for i in range(len(new)))

print(base64.b64encode(out).decode())
