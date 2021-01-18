#!/usr/bin/env python3
from PIL import Image
import sys

def imageconverter(x):
    im = Image.open(x).convert('RGBA')
    im.save(x+'.converted.png','png')
if len(sys.argv) > 1:
    print ("Files in progress: " + str(len(sys.argv[1:])))
    try:
        for x in sys.argv[1:]:
            imageconverter(x)
    except Exception:
        print("Error! Please check your input images")
        input("Press to continue...")
else:
    print("Drag and drop webp files to script")
    input("Press to continue...")