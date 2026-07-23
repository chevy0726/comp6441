# natas8 - Encoding is not encryption
# The secret was obscured with base64 -> string reversal -> hex.
# All three are reversible encodings with no key, so the original
# secret can be recovered by undoing each step in reverse order.

import codecs
import base64

# This encoded value is taken from the level's source code (fixed).
encoded_secret = "3d3d516343746d4d6d6c315669563362"

step1 = codecs.decode(encoded_secret, "hex")   # hex  -> bytes
step2 = step1[::-1]                              # reverse the bytes
final_secret = base64.b64decode(step2).decode("utf-8")  # base64 -> text

print(final_secret)   # -> oubWYf2kBq
