# import os, zipfile

# def backupToZip(folder):
#   folder = os.path.abspath(folder)
#   number = 1
#   while True:
#     zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
#     if not os.path.exists(zipFilename):
#       break;
#     number += 1

#     # TODO: create a ZIP file
#     print(f'Creating zip file name...')
#     backupZip = zipfile.ZipFile(zipFilename, 'w')
#     # TODO: Walk through entire folder tree and compress the files in each folder
#     for foldername, subfolders, filenames in os.walk(folder):
#       print(f'Adding files in {foldername}...')
#       backupZip.write(foldername)

#       for filename in filenames:
#         newBase = os.path.basename(folder) + '_'
#         if filename.startsWith(newBase) and filename.endswith('.zip'):
#           continue
#         backupZip.write(os.path.join(foldername, filename))
#     backupZip.close()
#     print('done')

# backupToZip('/home/engineer/Programming/CV')