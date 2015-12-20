import pyscreenshot as pyscreenshot
import dropbox

# part of the screen
# bbox=(startX, startY, endX, endY))
# im = pyscreenshot.grab(bbox=(3000, 0, 4000, 1080))
# im.save("printscreen.png", "PNG")

# grab full printscreen and save it to file
pyscreenshot.grab_to_file("printscreen.png")

# authenticate dropbox with access token
dbx = dropbox.Dropbox("access_token")
# read the file
file = open("printscreen.png", "rb").read()
# upload the file
dbx.files_upload(file, '/printscreenTIMESTAMP3.png')
# get url of uploaded file
fileUrl = dbx.sharing_create_shared_link("/printscreenTIMESTAMP3.png")
