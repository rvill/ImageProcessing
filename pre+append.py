# !/usr/bin/python
import os
import sys

#prepend at beginning of file
with open("raw_output.txt", "r+") as f:
    old = f.read()
    f.seek(0)
    f.write('import re\n')
    f.write('myString = """')
    f.close()

#append at end of file
with open("raw_output.txt", "a") as f:
    f.write(' """\n')
    f.write("urlList = re.findall(r'(https?://[^\s]+)', myString)\n")
    f.write("print urlList")
    f.close()

#rename file
os.rename("raw_output.txt","raw_output.py")

