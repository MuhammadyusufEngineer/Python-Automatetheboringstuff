#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
  # Get the address from command line
  address = ' '.join(sys.argv[1:])
else: 
  # Get the address from clipboard
  address = pyperclip.paste()

webbrowser.open('https://www.yandex.uz/maps/?text=' + address)