import dropbox
import sys
import time
import pyperclip
import subprocess
import os
# my packages
import vendor.config_loader.config as conf
import vendor.logger as logger

# app init
appPath = os.path.dirname(os.path.realpath(__file__))

# logger init
log = logger.Logger(appPath)
log.debug("Logger initialized")

# config init
config = conf.ConfigItems(appPath, "config")

filePath = '/'.join([config.get("Screenshot", "Path"), config.get("Screenshot", "Filename")])

# grab selected screen with SCROT backend
# need delay to properly run the scrot
time.sleep(0.01)
os.system("scrot -q %s -s %s" % (config.get("Screenshot", "Quality"), filePath,))

# authenticate dropbox with access token
dbx = dropbox.Dropbox(config.get("Dropbox", "AccessToken"))

# select the file to upload
openFile = open(filePath, "rb")
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
os.system("rm -rf %s" % (filePath,))

# show notification when file is uploaded properly
subprocess.Popen(['notify-send', "Url copied to clipboard!\n\r%s" % (fileUrl,)])

log.debug("Task completed")
