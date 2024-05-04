import csv
import os
from bs4 import BeautifulSoup

os.chdir(os.path.dirname(__file__))
with open("documentation.htm", "r") as file:
    doc = BeautifulSoup(file, "html.parser")

# get names of modules
names = [name.text for name in doc.find_all("code", class_="xref") if name.text not in ("concurrent","encodings","xmlrpc")]

# get description of modules
description = [desc.text for desc in doc.find_all("em")]

# get the link for mdodule's documentation
links = [link.get("href") for link in doc.find_all("a") if "library" in link.get("href")]

column_names = [("Module", "Description", "Documentation")]
with open("informations.csv", "w", newline="") as file:
    csv_file = csv.writer(file)
    csv_file.writerows(column_names)
    for ligne in list(zip(names, description, links)):
        csv_file.writerow(ligne)