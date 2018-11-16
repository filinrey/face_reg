#!/usr/bin/python

import face_recognition
import sys
import os
import re
from PIL import Image, ImageOps

TARGET_DIR = sys.path[0] + "/images/targets/"
IMAGE_WIDTH = 500
IMAGE_HEIGHT = 314


def resize_image(image, width, height):
    return
    img = Image.open(image)
    img = ImageOps.fit(img, (width, height), Image.ANTIALIAS)
    img.save(image + ".tmp.jpg")


test_image_name = "test_image.jpg"
if len(sys.argv) > 1:
    test_image_name = sys.argv[1]
resize_image(test_image_name, IMAGE_WIDTH, IMAGE_HEIGHT)
test_image = face_recognition.load_image_file(test_image_name)
test_encodings = face_recognition.face_encodings(test_image)
print "find", len(test_encodings), "faces"
'''
resize_image("./images/obama.jpg", IMAGE_WIDTH, IMAGE_HEIGHT)
obama2_image = face_recognition.load_image_file("./images/obama.jpg")
obama2_encoding = face_recognition.face_encodings(obama2_image)[0]

resize_image("./images/biden.jpg", IMAGE_WIDTH, IMAGE_HEIGHT)
trump1_image = face_recognition.load_image_file("./images/biden.jpg")
trump1_encoding = face_recognition.face_encodings(trump1_image)[0]
labels = ["obama", "biden"]

results = face_recognition.compare_faces([obama2_encoding, trump1_encoding], test_encodings[0], tolerance=0.6)
for i in range(len(results)):
    print results[i]
    if results[i] == True:
        print "you are", labels[i]
    else:
        print "you are not", labels[i]
    print "--"*32

exit()
'''
images = os.listdir(TARGET_DIR)
for j in range(len(test_encodings)):
    print "**"*10, "recognition", j+1, "people", "**"*10
    for image in images:
        name = re.match(r"(.+)\.jpg", image)
        if name == None:
            continue
        print "compare with", image
        resize_image(TARGET_DIR + image, IMAGE_WIDTH, IMAGE_HEIGHT)
        target_image = face_recognition.load_image_file(TARGET_DIR + image)
        target_encoding = face_recognition.face_encodings(target_image)[0]

        results = face_recognition.compare_faces([target_encoding], test_encodings[j], tolerance=0.6)
        for i in range(len(results)):
            print results[i]
            if  results[i] == True:
                print "\033[1;33;44myou are", name.group(1), "\033[0m"
            else:
                print "you are not", name.group(1)
            print "--"*32
    print ""

