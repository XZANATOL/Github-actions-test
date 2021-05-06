import sys
import json
import re


# Regex Patterns
category = r"- \[x\] (.+)"
name = r"Title: (.+)"
path = r"Folder: (.+)"
requirments_path = r"Requirments: (.+)"
entry = r"Script: (.+)"
arguments = r"Arguments: (.+)"
contributor = r"Contributor: (.+)"
description = r"Description: (.+)"


def add_script(category, name, path, entry, arguments, requirments_path, contributor, description):
    """ Add a Contributor script to database """

    new_data = {category: {name: [path, entry, arguments, requirments_path, contributor, description]}}
    data_store = read_data()
    
    try:
        # If category doesn't exist try will fail and except will ask to add a new category with the project
        if data_store[category]:                                          # Check for existing category or a new one
                data_store[category].update(new_data[category])           # Add script
    except:
        sure = "Y"
        sure = input("A new category is about to be added. You sure? Y/n > ")
        if sure.lower() == "y" or sure == "":
            data_store.update(new_data)                                     # Add new category
        else:
            print("Data wasn't added please re-run the script and add the correct inputs.")
            sys.exit(1)
        
    with open("datastore.json", "w") as file:
        json.dump(data_store, file)
    print("Script added to database")


def read_data():
    """ Loads datastore.json """
    with open("..\..\Master Script\datastore.json", "r") as file:
        data = json.load(file)
    return data


def extract_from_pr_body(pr_body):
    pr_body = pr_body[pr_body.index("## Project Metadata"):]
    category_list = []
    for text in pr_body:
        # <----- Validate Category ----->
        cat = re.match(category, text)
        if cat is not None:
            category_list.append(cat[1])
        # <----- Validate Title ----->
        if re.match(name, text) is not None:
            title = re.match(name, text)[1]
        # <----- Validate Folder ----->
        if re.match(path, text) is not None:
            folder = re.match(path, text)[1]
        # <----- Validate requirments.txt ----->
        if re.match(requirments_path, text) is not None:
            requirements = re.match(requirments_path, text)[1]
        # <----- Validate Script.py ----->
        if re.match(entry, text) is not None:
            script = re.match(entry, text)[1]
        # <----- Validate Arguments ----->
        if re.match(arguments, text) is not None:
            argument = re.match(arguments, text)[1]
        # <----- Validate Contribute ----->
        if re.match(contributor, text) is not None:
            user = re.match(contributor, text)[1]
        # <----- Validate Description ----->
        if re.match(description, text) is not None:
            desc = re.match(description, text)[1]

    # For GitHub Actions logging
    print("<----- MetaData ----->")
    print("Categories:", category_list)
    print("Title:", title)
    print("Path:", folder)
    print("Requirements:", requirements)
    print("Entry:", script)
    print("Arguments:",argument)
    print("Contributer:", user)
    print("Description:", desc)
    print("<----- ----- ----->")

    # The loop is for scripts that will be added to multiple categories
    #for cat in category_list:
    #    add_script(cat, title, folder, script, argument, requirements, user, desc)
    

if __name__ == "__main__":
    data = sys.argv[1]
    data = data.split("\n")
    for element in data:
        data[data.index(element)] = element.rstrip("\r")
    extract_from_pr_body(data)
