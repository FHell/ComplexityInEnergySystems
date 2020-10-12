#!/usr/bin/env python3

import os
import sys


list_of_names = []

for entry in os.scandir(os.getcwd()):
  if entry.is_file():
    with open(entry, 'r') as input_file:
      lines = input_file.read().splitlines()
    for line in lines:
      if line.startswith("name:"):
        list_of_names.append(line.lstrip("name:").split('#')[0].strip())

seen = {}
dupes = []

for x in list_of_names:
    if x not in seen:
        seen[x] = 1
    else:
        if seen[x] == 1:
            dupes.append(x)
        seen[x] += 1

if dupes:
  print(f"Duplicate name(s): {dupes}")
  print("aborting")
  sys.exit()


for entry in os.scandir(os.getcwd()):
  if entry.is_file():
    with open(entry, 'r') as input_file:
      lines = input_file.read().splitlines()
    rn_raw = ""
    grp_raw = ""
    for line in lines:
      if line.startswith("name:"):
        rn_raw = line.lstrip("name:").split('#')[0].strip()
    if rn_raw:
      os.rename(entry, f"{rn_raw}.md")
