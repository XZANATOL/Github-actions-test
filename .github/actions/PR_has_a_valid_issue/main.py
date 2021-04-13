import os

print("This is the PR body", os.getenv("prbody"))
print("*************************")
print(os.getenv("prbody"))
print("*************************")
print(type(os.getenv("prbody")))
