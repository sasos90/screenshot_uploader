import pyscreenshot as pyscreenshot

# part of the screen
# bbox=(startX, startY, endX, endY))
# im = pyscreenshot.grab(bbox=(3000, 0, 4000, 1080))
# im.save("printscreen.png", "PNG")

# grab full printscreen and save it to file
pyscreenshot.grab_to_file("printscreen.png")


