import codecs
import base64

encoded_secret = "3d3d516343746d4d6d6c315669563362"

step1 = codecs.decode(encoded_secret, "hex")   
step2 = step1[::-1]                              
final_secret = base64.b64decode(step2).decode("utf-8")  

print(final_secret)   # -> oubWYf2kBq
