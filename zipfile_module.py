import zipfile, os
from pathlib import Path
p = Path.home() / "Programming/assets/font"
exampleZip = zipfile.ZipFile(p / 'Roboto.zip')
# print(exampleZip.namelist())
spamInfo = exampleZip.getinfo('Roboto-VariableFont_wdth,wght.ttf')
# print(spamInfo.file_size)
# print(spamInfo.compress_size)
# print(f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!')
# exampleZip.extractall()

newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('egg.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()