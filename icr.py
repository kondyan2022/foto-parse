from icrawler.builtin import GoogleImageCrawler
from icrawler.builtin import BingImageCrawler

q = "ФОТО Центр Київ Київська область Україна"
num_pics = 10

google = GoogleImageCrawler(storage={"root_dir": "D:\\LoadPic"})
# filters = dict(size='large', license='commercial,modify')
# filters = dict(size='large')
# filters = dict(size='large')
filters = dict(type='photo')
google.crawl(keyword=q, filters=filters, max_num=10)

bing = BingImageCrawler(storage={"root_dir": "D:\\LoadPic\\bing"})

bing.crawl(keyword=q, filters=filters, max_num=10)
