# natas11 - Cryptographic failure (fixed-key XOR)
# The cookie is XOR-encrypted with a fixed key, then base64-encoded.
# XOR is symmetric: XOR of a known plaintext and its ciphertext gives
# back the key. The default JSON plaintext is public in the source, so
# the 4-byte key can be recovered and any cookie forged.

import base64

# NOTE: replace this with the "data" cookie value from your own browser
# session (it changes per session). Taken here from the Application panel.
c = base64.b64decode("EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0/GBlgaVVIJDURDSQ1VRY=")

# recover the repeating 4-byte key from the known default plaintext
key = [ord(p) ^ b for p, b in zip('{"showpassword":"no","bgcolor":"#ffffff"}', c)][:4]

# forge a new plaintext with showpassword set to yes
new = '{"showpassword":"yes","bgcolor":"#ffffff"}'
out = bytes(ord(new[i]) ^ key[i % 4] for i in range(len(new)))

# base64-encode the forged cookie, then paste it back into the browser
print(base64.b64encode(out).decode())
