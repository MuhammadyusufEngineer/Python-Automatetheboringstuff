# import shutil, os
# from pathlib import Path
# p = Path.home() / 'Programming/Python - Automatetheboringstuff/'

# # shutil.copy(p / 'spam.txt', p / 'some_folder')

# for filename in p.glob('capitalsquiz*.txt'):
#   os.unlink(filename)

# import send2trash

# baconFile = open('bacon.txt', 'a')
# baconFile.write('Bacon is not a vegetable')
# baconFile.close()

# send2trash.send2trash('bacon.txt')

import os
from pathlib import Path

for folderName, subfolders, filenames in os.walk(Path.home() / 'Programming/CV'):
  print('The curren folder is: ', folderName + ' ')

  for subfolder in subfolders:
    print('SUBFOLDER OF :' + folderName + " " + subfolder)
  
  for filename in filenames:
    print('FILE INSIDE: ' + folderName + ' ' + filename)

