import pyscreenshot as pyscreenshot
import dropbox
import sys
import time

# part of the screen
# bbox=(startX, startY, endX, endY))
# im = pyscreenshot.grab(bbox=(3000, 0, 4000, 1080))
# im.save("printscreen.png", "PNG")

# grab full printscreen and save it to file
pyscreenshot.grab_to_file("printscreen.png")

# authenticate dropbox with access token
dbx = dropbox.Dropbox("access_token")
# read the file
openFile = open("printscreen.png", "rb")
fileToUpload = openFile.read()
# upload the file
uploadFileName = "/printscreen%s.png" % (time.time(),)
dbx.files_upload(fileToUpload, uploadFileName)
# get url of uploaded file
metaData = dbx.sharing_create_shared_link(uploadFileName)
fileUrl = metaData.url
