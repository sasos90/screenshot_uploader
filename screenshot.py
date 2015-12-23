import pyscreenshot
import dropbox
import sys
import time
import pyperclip
import subprocess
import os

# part of the screen
# bbox=(startX, startY, endX, endY))
# im = pyscreenshot.grab(bbox=(3000, 0, 4000, 1080))
# im.save("printscreen.png", "PNG")

# grab full printscreen and save it to file
# pyscreenshot.grab_to_file("printscreen.png")

# grab selected screen with SCROT backend
os.system("scrot -s printscreen.png");

# authenticate dropbox with access token
dbx = dropbox.Dropbox("4I36gE2ePRAAAAAAAAAAH_aIfXX0hvrFEA9HyuSGyrOHuUQo281LJz9rLiiqmsDm")
# read the file
openFile = open("printscreen.png", "rb")
fileToUpload = openFile.read()
# upload the file
uploadFileName = "/printscreen%s.png" % (time.time(),)
dbx.files_upload(fileToUpload, uploadFileName)
# get url of uploaded file
metaData = dbx.sharing_create_shared_link(uploadFileName)
fileUrl = metaData.url

# copy file url to clipboard
pyperclip.copy(fileUrl)

# delete printscreenfile
os.system("rm -rf printscreen.png")

# show notification when file is uploaded properly
subprocess.Popen(['notify-send', "Url copied to clipboard!\n\r%s" % (fileUrl,)])
