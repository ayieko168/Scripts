from ast import While
import string
import random
import os
import shutil
from tkinter import E, PIESLICE
from turtle import back

PREFIX = "aces_tech_"
RANDOM_STR_LEN = 8

welcome_message = f"\n\n\n{'#'*90}\nThis script will rename files to whatever you want them to.\nYou can rename a whole directory of images or just one image file.\n{'#'*90}\n"
print(welcome_message)

## Get operation to do
numbering = input(">>> Enter the mode of numbering you want to use...\n1) Random generated\n2) Sequential Numerical numbering (001, 002, 003, etc)\n(1 Default) >>> ")
if not numbering.strip(): numbering = "1"
if not numbering.isdigit():
    print("--> Select a valid option (1 or 2)")
    exit()
if int(numbering) > 2:
    print("--> Select a valid option (1 or 2)")
    exit()
print(f"--> You chose option # {numbering}\n")

# ## Prefix or Surfix
# pref_surf = input(">>> Enter a prefix or serfix to be used in the naming of the files. (Default None)\nSyntax: pref <PREFIX STRING> or surf <SURFIX STRING> or pref <PREFIX STRING> surf <SURFIX STRING> to apply both \n>>> ")
# if pref_surf.strip() == '':
#     print("--> Not Appling any preffix or suffix")
# elif 'pref' in pref_surf:


## Setting the file or path
while True:
    ops_path = input(">>> Now enter the full path to the directory/file you want to operate on...\n>>> ")
    if os.path.isabs(ops_path):
        break
    else:
        print("The path you entered does not exist, try again.\n")

## Ops summary
confirmation = input("Do you want to continue?\n1) Yes\n2) No\n(Default 1)>>> ")
if not confirmation.strip(): confirmation = "1"
if not confirmation.isdigit():
    print("--> Select a valid option (1 or 2)")
    exit()
if int(confirmation) > 2:
    print("--> Select a valid option (1 or 2)")
    exit()

print(f"--> You chose option # {confirmation}\n")

if confirmation == '2':
    exit()

## rename operation
if os.path.isfile(ops_path):
    src_path = ops_path
    
    if numbering == "1":
        base = os.path.dirname(ops_path)
        name = "image_" + "".join(random.choices(string.ascii_letters, k=RANDOM_STR_LEN))
        extension = os.path.splitext(ops_path)[-1]
        ## Apply suffix and prfix logic here ##
 
        dst_path = os.path.join(base, "Renamed", name+extension)
        if not os.path.isdir(os.path.dirname(dst_path)): os.makedirs(os.path.dirname(dst_path))
        print(f"New Dir: {dst_path}")

    shutil.copy2(ops_path, dst_path)

    print("Done all operations")
    exit()

elif os.path.isdir(ops_path):
    files = [os.path.join(ops_path, f) for f in os.listdir(ops_path) if os.path.isfile(os.path.join(ops_path, f))]
    print(f"Applying opertaion on {len(files)} files bellow... ")
    for i, file in enumerate(files): print(f"{i}) {file}")

    print("\n")
    for i, file in enumerate(files):

        base = os.path.dirname(file)
        name = PREFIX + "".join(random.choices(string.ascii_letters, k=RANDOM_STR_LEN))
        extension = os.path.splitext(file)[-1]
        ## Apply suffix and prfix logic here ##
 
        dst_path = os.path.join(base, "Renamed", name+extension)
        if not os.path.isdir(os.path.dirname(dst_path)): os.makedirs(os.path.dirname(dst_path))
        print(f"{i}) New file path: {dst_path}")

        shutil.copy2(file, dst_path)






















