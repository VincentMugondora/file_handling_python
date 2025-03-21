import os

# os.remove("dummy.txt")

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

# delete a folder
os.rmdir("myfolder")