import dropbox
import sys
import time
import pyperclip
import subprocess
import os
import config_loader.config as conf

appPath = os.path.dirname(os.path.realpath(__file__))
config = conf.ConfigItems(appPath, "config")
config.get("PathInfo", "ScreenshotPath")

filePath = '/'.join([config.get("PathInfo", "ScreenshotPath"), config.get("PathInfo", "ScreenshotFilename")])

# grab selected screen with SCROT backend
# need delay to properly run the scrot
time.sleep(0.01)
os.system("scrot -s %s" % (filePath,))

# authenticate dropbox with access token
dbx = dropbox.Dropbox(config.get("Dropbox", "AccessToken"))

fileExists = False
counter = 0
fileToUpload = False
while fileExists is False and counter < 5:
    if os.path.isfile(filePath) is True:
        # read the file
        openFile = open(filePath, "rb")
        fileToUpload = openFile.read()
        fileExists = True
    else:
        counter += 1
        time.sleep(0.5)

# upload the file
uploadFileName = "/printscreen%s.png" % (time.time(),)
dbx.files_upload(fileToUpload, uploadFileName)
# get url of uploaded file
metaData = dbx.sharing_create_shared_link(uploadFileName)
fileUrl = metaData.url

# copy file url to clipboard
pyperclip.copy(fileUrl)

# delete printscreenfile
os.system("rm -rf %s" % (filePath,))

# show notification when file is uploaded properly
subprocess.Popen(['notify-send', "Url copied to clipboard!\n\r%s" % (fileUrl,)])
