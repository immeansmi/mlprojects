import os
from pathlib import Path
import logging
filepath1 = f"D:\chromedriver_win32\chromedriver.exe"
filepath = Path(filepath1)
filedir, filename = os.path.split(filepath1)
print(filedir, filename)

# if filedir != "":
#     os.makedirs(filedir, exist_ok=True)
#     logging.info(f"Creating directory:{filedir} for the file {filename}")
#
#
# if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
#     with open (filepath, 'w') as f:
#         pass
#         logging.info(f"Creating empty file: {filepath}")
#
# else:
#     logging.info(f"{filename} already exists")
