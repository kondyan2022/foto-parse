import os
from pathlib import Path
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv
load_dotenv()


print(os.getenv('CLOUD_NAME'),
      os.getenv('API_KEY'),
      os.getenv('API_SECRET'))
cloudinary.config(cloud_name=os.getenv('CLOUD_NAME'),
                  api_key=os.getenv('API_KEY'),
                  api_secret=os.getenv('API_SECRET'))


# upload_data = cloudinary.uploader.upload(file)


def upload2cloudinary(filepath, folder):
    for infile in filepath.glob("*.[jpg jpeg png gif webp]*"):
        upload_data = cloudinary.uploader.upload(
            infile, folder=folder, use_filename=True, unique_filename=False, overwrite=True)
        print(f'finish upload {infile.name}')
