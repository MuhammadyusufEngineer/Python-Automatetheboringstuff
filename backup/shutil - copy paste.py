import shutil, os
from pathlib import Path
p = Path.home() / 'Programming/Automatetheboringstuff/spam.txt'

shutil.copy(p / 'spam.txt', p / 'some_folder')