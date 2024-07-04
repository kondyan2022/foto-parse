from PIL import Image, ImageFile
import glob
import os
ImageFile.LOAD_TRUNCATED_IMAGES = True

for infile in glob.glob("d:\\LoadPic\\*.jpg")+glob.glob("d:\\LoadPic\\*.png")+glob.glob("d:\\LoadPic\\*.gif"):
    file, ext = os.path.splitext(infile)
    print(file, ext)
    im = Image.open(infile).convert("RGB")
    im.save(file + ".webp", "webp")
