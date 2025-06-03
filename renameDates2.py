import shutil, os, re

datePattern = re.compile(r"""^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$""", re.VERBOSE)

for amerFilename in os.listdir('./renameDates'):
  mo = datePattern.search(amerFilename)

    # Skip files without a date.
  if mo == None:
    continue

  # Get the different parts of the filename.
  beforePart = mo.group(1)
  monthPart  = mo.group(2)
  dayPart    = mo.group(4)
  yearPart   = mo.group(6)
  afterPart  = mo.group(8)

  euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

     # Get the full, absolute file paths.
  absWorkingDir = os.path.abspath('./renameDates')
  amerFilename = os.path.join(absWorkingDir, amerFilename)
  euroFilename = os.path.join(absWorkingDir, euroFilename)

     # Rename the files.
  # print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
  shutil.move(amerFilename, euroFilename)   # uncomment after testing