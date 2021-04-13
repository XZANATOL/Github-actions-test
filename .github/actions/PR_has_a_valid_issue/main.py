import os, re

pattern = "#\d+"  # Used pattern to search for Issues.

body = os.getenv("INPUT_PRBODY")  # PR body
url  = os.getenv("INPUT_PRURL")   # PR URL

issue = re.search(pattern, body)[0].replace("#", "")
print(issue)
print(url)
