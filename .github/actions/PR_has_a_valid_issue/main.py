import os, re

pattern = "#\d+"  # Used pattern to search for Issues.

body = os.getenv("INPUT_PRBODY")  # PR body
url  = os.getenv("INPUT_PRURL")   # PR URL

issue_num = re.search(pattern, body)[0].replace("#", "")

# url list will be something like this
# ['https:', '', 'api.github.com', 'repos', 'owner', 'repo-name']
url = url.split("/")[:-2]               # Split URL using slashes
url[2] = url[2].replace("api", "www")   # Replace API URL with HTML URL
url.pop(3)                              # Get rid of "repos" record
url = "/".join(url)                     # Reattach URL pieces
url += "/issues/{}".format(issue_num)   # Add issue number
print(url)
