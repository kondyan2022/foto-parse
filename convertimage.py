from PIL import Image, ImageFile
from pathlib import Path
import os
ImageFile.LOAD_TRUNCATED_IMAGES = True


def shrink_file(filepath):
    im = Image.open(filepath)
    half = 0.5
    im = im.resize([int(half * s) for s in im.size])
    im.save(filepath, im.format)


def pic2webp(path):
    for infile in path.glob("*.[jpg jpeg png gif]*"):
        filename, ext = os.path.splitext(infile)
        im = Image.open(infile).convert("RGB")
        im.save(filename + ".webp", "webp")
        newFile = Path(filename + ".webp")
        current_file, unlink_file = (newFile, infile) if newFile.stat(
        ).st_size <= infile.stat().st_size else (infile, newFile)
        unlink_file.unlink()
        while current_file.stat().st_size > 500000:
            shrink_file(current_file)
