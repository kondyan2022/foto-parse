from pathlib import Path
from upload2cloudinary import upload2cloudinary
from convertimage import pic2webp_single
from crawler import load_images
from parse import get_state_dict
import sys
import os
from dotenv import load_dotenv
load_dotenv(override=True)


FILENAME = sys.argv[1]
CLOUD_ROOT_FOLDER = os.getenv('CLOUD_ROOT_FOLDER')
SEARCH_LANG = os.getenv('SEARCH_LANG')
COUNTRY = os.getenv('COUNTRY')
PHOTO = {'uk': 'фото', 'ru': 'фото', 'en': 'photo', 'pl': 'zdjęcie'}
NUM_PICS = int(os.getenv('NUM_PICS'))

google = (sys.argv[2] if len(sys.argv) > 2 else None) == 'google'


if len(FILENAME) == 0:
    exit()


def get_image(q, local_path, cloud_path, filename):
    load_images(q=q, path=local_path, num_pics=1, google=google)
    pic2webp_single(local_path, filename)


def main():
    country, state, cities = get_state_dict(FILENAME)

    path_dir_country = Path('.').absolute() / 'images' / country['en']
    path_dir_state = path_dir_country / state['en']
    q = f'{PHOTO[SEARCH_LANG]} {state[SEARCH_LANG]} {country[SEARCH_LANG]}'
    state_cloud_dir = f'{CLOUD_ROOT_FOLDER}/{country['en']}/{state['en']}/'
    get_image(q, path_dir_state, state_cloud_dir, state['en'])
    upload2cloudinary(path_dir_state, state_cloud_dir)

    for item in cities[0:2]:
        q = f'{PHOTO[SEARCH_LANG]} {item[SEARCH_LANG]} {
            state[SEARCH_LANG]} {country[SEARCH_LANG]}'
        path_dir_city = path_dir_state / item['en']
        city_cloud_dir = f'{state_cloud_dir}{item['en']}/'

        get_image(q, path_dir_city, city_cloud_dir, item['en'])

        for district in item['districts']:
            q = f'{PHOTO[SEARCH_LANG]} {district[SEARCH_LANG]} {item[SEARCH_LANG]} {
                state[SEARCH_LANG]} {country[SEARCH_LANG]}'
            get_image(q, path_dir_city, city_cloud_dir, district['en'])

        upload2cloudinary(path_dir_city, city_cloud_dir)


if __name__ == "__main__":
    main()
