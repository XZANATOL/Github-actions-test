import os

print("This is the PR body", os.getenv("INPUT_PRBODY"))
print("*************************")
print(os.getenv("INPUT_PRBODY"))
print("*************************")
print(type(os.getenv("INPUT_PRBODY")))
