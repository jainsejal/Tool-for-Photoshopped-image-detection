#!/usr/bin/env python

__author__ = 'Sejal Jain'
from PIL import Image
from PIL.ExifTags import TAGS
import CopyMoveDetection
import sys

if (len(sys.argv) < 2):
    print "[-] Please enter an image file path"
    print "[-] USAGE: $ ./ForensicsTool imagepath"
    print "[-] Program Exiting."
    exit()

imagefile = sys.argv[1]

try:
    myimg = Image.open(imagefile)
    #imgfile = open(imagefile, 'rb')
except:
    print "[-] Image could not be opened. Please check the image file path."
    print "[-] Program Exiting." 
    exit();


def get_exif_tags(myimg):
    #print "in get exif tags"
    try:
        ret = {}
        info = myimg._getexif()
        #print type(info)
        for tag in info.keys():
            #print "in info.keys"
            if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                if tag == 'Image Software':
                    print "[-] Software used: %s" % (tags[tag])

        for tag, value in info.items():
            #print "in info.items"
            decoded = TAGS.get(tag, tag)
            #print "decoded"
            ret[decoded] = value
            #print type(ret)
        return ret
    except:
        #print "in except"
        print "[-] Exif data not found. The Image might be edited."
        exit();

    

image_data = get_exif_tags(myimg)


# Exif tests to detect originality of the image
try:
    print "[-] Analysing Exif Data"
    # initializing isoriginal flag as false
    isoriginal = False
    
    # Checking the image's date time tag
    print "[-] Checking the image's date time tag."
    if(image_data['DateTime'] == image_data['DateTimeOriginal']):
        # setting isoriginal flag as true
        isoriginal = True
        
    # Checking if exif data contains information about the most popular image editing tools
    print "[-] Checking the image's Software tag."
    if(('photoshop' in image_data['Software'].lower()) or \
       ('adobe' in image_data['Software'].lower()) or \
       ('pixel' in image_data['Software'].lower()) or \
       ('google' in image_data['Software'].lower()) or \
       ('lightroom' in image_data['Software'].lower()) or \
       ('aviary' in image_data['Software'].lower()) or \
       ('luminar' in image_data['Software'].lower()) or \
       ('affinity' in image_data['Software'].lower()) or \
       ('paintshop' in image_data['Software'].lower()) or \
       ('acorn' in image_data['Software'].lower()) or \
       ('elements' in image_data['Software'].lower()) or \
       ('DxO' in image_data['Software'].lower()) or \
       ('photolab' in image_data['Software'].lower()) or \
       ('snapseed' in image_data['Software'].lower()) or \
       ('vsco' in image_data['Software'].lower()) or \
       ('afterlight' in image_data['Software'].lower()) or \
       ('enlight' in image_data['Software'].lower()) or \
       ('touchretouch' in image_data['Software'].lower()) or \
       ('instagram' in image_data['Software'].lower()) or \
       ('mextures' in image_data['Software'].lower()) or \
       ('lensdistortions' in image_data['Software'].lower()) or \
       ('superimpose' in image_data['Software'].lower())
      ): 
        # setting soriginal flag as false
        isoriginal = False

    
    if(isoriginal == False):
        # Check copy-move edits in the image
        print "[-] Checking copy-move edits in the image."
        status = CopyMoveDetection.detect(imagefile)
        print '[-] Exif Checks and Copy-Move Detection Status :' + status
        print '[-] The image seems to be edited.'
    else:
        # Check copy-move edits in the image
	status = CopyMoveDetection.detect(imagefile)
        print '[-] Exif Checks and Copy-Move Detection Status :' + status
        #print '[-] The image seems to be original.'

except:
    #print 'inside except'
    print "[-] There was an error while verifying the image. The image might be tampered."
