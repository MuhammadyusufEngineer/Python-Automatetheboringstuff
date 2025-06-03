#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

# 1
##### Remove existing files (if exists)
# import os
# from pathlib import Path
# for file in os.listdir(Path.cwd() / 'renameDates'):
#   os.unlink(Path.cwd() / 'renameDates' / file)

# 2
##### Create American style date files

# from pathlib import Path
# targetFolder = Path.home() / 'Programming/Python - Automatetheboringstuff/renameDates'

# for month in range(12):
#   for day in range(31):
#     # print(str(month + 1) + " " + str(day + 1))/
#     filename = f"{month + 1}-{day + 1}-2025.txt"
#     filepath = targetFolder / filename
#     dayFile = open(filepath, 'w')
#     dayFile.write(f'Hello from {day + 1} file')
#     dayFile.close()

# 3 
####### Convert American files into european

# import shutil, os, re

# datePattern = re.compile(r"""^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$""", re.VERBOSE)

# for amerFilename in os.listdir('./renameDates'):
#   mo = datePattern.search(amerFilename)

#   if mo == None:
#     continue

#   beforePart = mo.group(1)
#   monthPart = mo.group(2)
#   dayPart = mo.group(4)
#   yearPart = mo.group(6)
#   afterPart = mo.group(8)

#   euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

#   absWorkingDir = os.path.abspath('./renameDates')
#   amerFilename = os.path.join(absWorkingDir, amerFilename)
#   euroFilename = os.path.join(absWorkingDir, euroFilename)

#   shutil.move(amerFilename, euroFilename)