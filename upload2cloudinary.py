import os
from pathlib import Path
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv
load_dotenv()


cloudinary.config(cloud_name=os.getenv('CLOUD_NAME'),
                  api_key=os.getenv('API_KEY'),
                  api_secret=os.getenv('API_SECRET'))


def upload2cloudinary(filepath, folder):
    for infile in filepath.glob("*.[jpg jpeg png gif webp]*"):
        cloudinary.uploader.upload(
            infile, public_id=infile.stem, folder=folder, use_filename=True, unique_filename=False, overwrite=True)
        print(f'finish upload {infile.name}')
