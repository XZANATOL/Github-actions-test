import os

print("This is the PR body", os.getenv("pr_body"))
print("*************************")
print(os.getenv("pr_body"))
print("*************************")
print(type(os.getenv("pr_body")))
