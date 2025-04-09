import httpx
from src.deobfuscator import AST


# https://www.cloudflare.com/en-gb/
# https://www.cloudflare.com/cdn-cgi/challenge-platform/scripts/jsd/main.js

req = httpx.get("https://www.cloudflare.com/cdn-cgi/challenge-platform/scripts/jsd/main.js", follow_redirects=True)
print(req.text)

deobf = AST().deobfuscate(req.content)
with open("./deobf/deobfuscated.js", "w") as f:
    f.write(deobf)
# print(deobf)
