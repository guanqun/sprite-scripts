#!/usr/bin/env python
#
# combine 9 sprites into one sprite, useful for CCScale9Sprite class.
#

import Image
import sys

if len(sys.argv) != 2:
    print "Please specify the base file name!"
    sys.exit(-1)

basefile = sys.argv[1]

try:
    lefttop = Image.open(basefile + '_lefttop.png')
    top = Image.open(basefile + '_top.png')
    righttop = Image.open(basefile + '_righttop.png')
    left = Image.open(basefile + '_left.png')
    center = Image.open(basefile + '_center.png')
    right = Image.open(basefile + '_right.png')
    leftbottom = Image.open(basefile + '_leftbottom.png')
    bottom = Image.open(basefile + '_bottom.png')
    rightbottom = Image.open(basefile + '_rightbottom.png')
except:
    print "Make sure all files are there!"
    sys.exit(-1)

# sanity check
sanity = False
if lefttop.size[0] == left.size[0] and lefttop.size[0] == bottom.size[0] and top.size[0] == center.size[0] and top.size[0] == bottom.size[0] and righttop.size[0] == right.size[0] and righttop.size[0] == bottom.size[0]:
    if lefttop.size[1] == top.size[1] and lefttop.size[1] == righttop.size[1] and left.size[1] == center.size[1] and left.size[1] == right.size[1] and leftbottom.size[1] == bottom.size[1] and leftbottom.size[1] == rightbottom.size[1]:
        sanity = True

#if sanity == False:
#    print "the size of all these pictures doens't match!"
#    sys.exit(-1)

width  = lefttop.size[0] + center.size[0] + rightbottom.size[0]
height = lefttop.size[1] + center.size[1] + rightbottom.size[1]

tim = Image.new('RGBA', (width, height))

offset_0 = (0, 0)
offset_1 = lefttop.size
offset_2 = (lefttop.size[0] + center.size[0], lefttop.size[1] + center.size[1])

tim.paste(lefttop,      (offset_0[0], offset_0[1]))
tim.paste(top,          (offset_1[0], offset_0[1]))
tim.paste(righttop,     (offset_2[0], offset_0[1]))

tim.paste(left,         (offset_0[0], offset_1[1]))
tim.paste(center,       (offset_1[0], offset_1[1]))
tim.paste(right,        (offset_2[0], offset_1[1]))

tim.paste(leftbottom,   (offset_0[0], offset_2[1]))
tim.paste(bottom,       (offset_1[0], offset_2[1]))
tim.paste(rightbottom,  (offset_2[0], offset_2[1]))

tim.save(basefile + '_one.png', 'PNG')
