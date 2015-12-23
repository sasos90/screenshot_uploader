import pyscreenshot
import dropbox
import sys
import time
import pyperclip
import subprocess
import os
import os.path
import ConfigParser

# load config file
Config = ConfigParser.ConfigParser()
Config.read("%s/config.ini" % (os.path.dirname(os.path.realpath(__file__)),))

# get values from config file
_SCREENSHOT_PATH = Config.get("PathInfo", "ScreenshotPath")
_SCREENSHOT_FILENAME = Config.get("PathInfo", "ScreenshotFilename")
_ACCESS_TOKEN = Config.get("Dropbox", "AccessToken")

fullFilePath = '/'.join([_SCREENSHOT_PATH, _SCREENSHOT_FILENAME])

# grab selected screen with SCROT backend
os.system("scrot -s %s" % (fullFilePath,));

# authenticate dropbox with access token
dbx = dropbox.Dropbox(_ACCESS_TOKEN)

fileExists = False
counter = 0
fileToUpload = False
while fileExists is False and counter < 5:
    if os.path.isfile(fullFilePath) is True:
        # read the file
        openFile = open(fullFilePath, "rb")
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
os.system("rm -rf %s" % (fullFilePath,))

# show notification when file is uploaded properly
subprocess.Popen(['notify-send', "Url copied to clipboard!\n\r%s" % (fileUrl,)])
