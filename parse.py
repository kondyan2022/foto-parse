
import re
from transliterate import translit, get_available_language_codes


LANGUAGES = ['uk', 'ru', 'en', 'pl']
LANG_FULLNAME = ['українська', 'російська', 'англійська', 'польська']
LANG_ZIP = dict(zip(LANG_FULLNAME, LANGUAGES))
STATES = {'wait_city', 'wait_lang', 'wait_districts'}


def get_city(text):
    cities = [elem.strip().lower() for elem in text.split(' / ')]
    if len(cities) == 4:
        return True, dict(zip(LANGUAGES, cities))
    return False, None


def get_language(text):
    lang = text.strip().lower().rstrip(":")
    if lang in LANG_FULLNAME:
        return True, LANG_ZIP[lang]
    return False, None


def get_district(text):
    match = re.search(r'^(\d+\.\d+\.)\s{1}(.+)$', text.strip())
    if match:
        return True, match[1][:-1], match[2].lower()
    return False, None, None


def get_state_dict(filename):
    cities = []
    current_city = ''
    current_lang = ''
    with open(filename, "r", encoding='utf-8') as file:
        fc = file.readlines()
    flag, country = get_city(fc[0])
    flag, state = get_city(fc[1])

    for line in fc[2:]:
        flag, value = get_city(line)
        if flag:
            if current_city != '':
                cities.append(current_city)
            current_city = value.copy()
            current_city['districts'] = []
            continue
        flag, value = get_language(line)
        if flag:
            current_lang = value
            continue
        flag, id, value = get_district(line)
        if flag:
            elem = _[0] if (_ := [x for x in current_city['districts']
                                  if x['id'] == id]) else None
            if elem:
                elem[current_lang] = value
            else:
                current_city['districts'].append(
                    {"id": id, current_lang: value})
    cities.append(current_city)

    return country, state, cities
