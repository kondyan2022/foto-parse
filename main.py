# import requests
# # from bs4 import BeautifulSoup

# url = "https://www.google.com/search?q=фото+Ужгород&tbm=isch"

# headers = {"Accept": "*/*",
#            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
#            }

# req = requests.get(url, headers=headers)
# src = req.text
# # print(src)

# with open('index.html', "w") as file:
#     file.write(src)
import requests
from bs4 import BeautifulSoup


def scrape_images(location):
    search_url = f"https://www.google.com/search?tbm=isch&q={location}"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}
    response = requests.get(search_url, headers=headers)
    # print(response.text)
    # with open('response.html', "w") as file:
    #     file.write(response.text)
    soup = BeautifulSoup(response.text, 'lxml')
    images = [img['src'] for img in soup.find_all('img', {'src': True})]
    return images

    # # Приклад використання
location = "Katowice Poland"
images = scrape_images(location)

print(images)
