#!/usr/bin/env python
#
# We assume there are FILE.png and FILE.xml.
# We align the sprites to have the same width and height.

import sys
import xml
from xml.dom.minidom import parseString

if len(sys.argv) != 2:
    print "Please specify the file name!"
    sys.exit(-1)

filename = open(sys.argv[1], 'r')
filedata = filename.read()
filename.close()

basefilename = sys.argv[1].split('.')[0]

try:
    dom = parseString(filedata)
except:
    print "Make sure the xml file is valid!"
    sys.exit(-1)

allframes = dom.getElementsByTagName('img')

leftarray = []
rightarray = []
toparray = []
bottomarray = []
framenames = []
cropbox = []

for frame in allframes:
    leftarray.append(int(frame.getAttribute('ox')))
    toparray.append(int(frame.getAttribute('oy')))
    rightarray.append(int(frame.getAttribute('w')) - int(frame.getAttribute('ox')))
    bottomarray.append(int(frame.getAttribute('h')) - int(frame.getAttribute('oy')))
    framenames.append(basefilename + '_' + frame.getAttribute('name').split('_')[1])
    cropbox.append((int(frame.getAttribute('x')), int(frame.getAttribute('y')),
                    int(frame.getAttribute('x')) + int(frame.getAttribute('w')), int(frame.getAttribute('y')) + int(frame.getAttribute('h'))))

leftmax = max(leftarray)
rightmax = max(rightarray)
topmax = max(toparray)
bottommax = max(bottomarray)

width = leftmax + rightmax
height = topmax + bottommax

print "left pixels: ", leftarray
print "right pixels: ", rightarray
print "top pixels: ", toparray
print "bottom pixels: ", bottomarray
print "frame names: ", framenames
print "width: ", width
print "height: ", height

import Image

imagefilename = basefilename + '.png'

try:
    im = Image.open(imagefilename)
except:
    print "can't find image file: ", imagefilename
    sys.exit(-1)

for i in range(len(leftarray)):
    framename = framenames[i]
    part = im.crop(cropbox[i])

    tim = Image.new('RGBA', (width, height))
    tim.paste(part, (leftmax - leftarray[i], topmax - toparray[i]))
    tim.save(framename, 'PNG')

print "anchor point (normal):  ", float(leftmax) / float(width), " ", float(bottommax) / float(height)
print "anchor point (flipped): ", 1.0 - float(leftmax) / float(width), " ", float(bottommax) / float(height)

