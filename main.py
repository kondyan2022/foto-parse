from pathlib import Path
from upload2cloudinary import upload2cloudinary
from convertimage import pic2webp
from crawler import load_images
from parse import get_state_dict
import sys
import os
from dotenv import load_dotenv
load_dotenv()


FILENAME = sys.argv[1]
google = (sys.argv[2] if len(sys.argv) > 2 else None) == 'google'
CLOUD_ROOT_FOLDER = os.getenv('CLOUD_ROOT_FOLDER')
SEARCH_LANG = os.getenv('SEARCH_LANG')
COUNTRY = os.getenv('COUNTRY')
PHOTO = {'uk': 'фото', 'ru': 'фото', 'en': 'photo', 'pl': 'zdjęcie'}

print(CLOUD_ROOT_FOLDER)

if len(FILENAME) == 0:
    exit()

state, state_trans, cities = get_state_dict(FILENAME)

for item in cities[0:2]:
    q = f'{PHOTO[SEARCH_LANG]} {item[SEARCH_LANG]} {state} {COUNTRY}'
    path_dir = Path('.').absolute() / 'images' / state_trans / item['en']
    print(path_dir)
    load_images(q=q, path=path_dir, num_pics=5, google=google)
    pic2webp(path_dir)
    upload2cloudinary(
        path_dir, f'{CLOUD_ROOT_FOLDER}/{state_trans}/{item['en'].replace(' ', '_')}/main/')
    for district in item['districts']:
        q = f'Фото {district[SEARCH_LANG]} {
            item[SEARCH_LANG]} {state} {COUNTRY}'
        path_dir = Path('.').absolute() / 'images' / \
            state_trans / \
            item['en'].replace(' ', '_') / district['en'].replace(' ', '_')
        load_images(q=q, path=path_dir, num_pics=5, google=google)
        pic2webp(path_dir)
        upload2cloudinary(
            path_dir, f'/{CLOUD_ROOT_FOLDER}/{state_trans}/{item['en'].replace(' ', '_')}/{district['en'].replace(' ', '_')}/')
