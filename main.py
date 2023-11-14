import urllib.request
import string
import numpy as np
from PIL import Image
import cv2

char = string.ascii_lowercase
file_code_name = {}

width = 50
height = 0
newwidth = 0
arr = string.ascii_letters
arr = arr + string.digits + "+,.-? "
letss = string.ascii_letters


def getimg(case, col):
    global width, height, back
    try:
        url = (
            "https://raw.githubusercontent.com/Ankit404butfound/HomeworkMachine/master/Image/%s.png"
            % case
        )
        imglink = urllib.request.urlopen(url)
    except:
        url = (
            "https://raw.githubusercontent.com/Ankit404butfound/HomeworkMachine/master/Image/%s.PNG"
            % case
        )
        imglink = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imglink.read()))
    img = cv2.imdecode(imgNp, -1)
    cv2.imwrite(r"%s.png" % case, img)
    img = cv2.imread("%s.png" % case)
    img[np.where((img != [255, 255, 255]).all(axis=2))] = col
    cv2.imwrite("chr.png", img)
    cases = Image.open("chr.png") 
    back.paste(cases, (width, height))
    newwidth = cases.width
    width = width + newwidth


def text_to_handwriting(string, rgb=[0, 0, 138], save_to: str = "pywhatkit.png"):
    """Convert the texts passed into handwritten characters"""
    global arr, width, height, back
    try:
        back = Image.open("zback.png")
    except:
        url = "https://raw.githubusercontent.com/Ankit404butfound/HomeworkMachine/master/Image/zback.png"
        imglink = urllib.request.urlopen(url)
        imgNp = np.array(bytearray(imglink.read()))
        img = cv2.imdecode(imgNp, -1)
        cv2.imwrite("zback.png", img)
        back = Image.open("zback.png")
    rgb = [rgb[2], rgb[1], rgb[0]]
    count = -1
    lst = string.split()
    for letter in string:
        if width + 150 >= back.width or ord(letter) == 10:
            height = height + 227
            width = 50
        if letter in arr:
            if letter == " ":
                count += 1
                letter = "zspace"
                wrdlen = len(lst[count + 1])
                if wrdlen * 110 >= back.width - width:
                    width = 50
                    height = height + 227

            elif letter.isupper():
                letter = "c" + letter.lower()
            elif letter == ",":
                letter = "coma"
            elif letter == ".":
                letter = "fs"
            elif letter == "?":
                letter = "que"

            getimg(letter, rgb)

    back.save(f"{save_to}")
    back.close()
    back = Image.open("zback.png")
    width = 50
    height = 0
    return save_to








######################
# import pywhatkit as pw

# # ####
# # Convert Text to HandWriting Text
# # askUser = input('Enter Text to change : ')
# txt = """This is my text now chnage"""

# pw.text_to_handwriting(txt)

# print('--- Conversion Done ---')

# ####
# Send WhatsApp Message
# try:
#     pw.sendwhatmsg_instantly("+91XXXXXXX", "hello", 15)
#     print("Successfully Sent!")
# except:
#     print("An Unexpected Error!")