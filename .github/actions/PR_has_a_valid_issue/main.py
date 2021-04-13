import os, re

pattern = "#\d+"

body = os.getenv("INPUT_PRBODY")
print("*************************")
print(body)
print("*************************")
print(re.search(pattern, body))
