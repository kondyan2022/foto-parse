from icrawler.builtin import GoogleImageCrawler
from icrawler.builtin import BingImageCrawler


def load_images(q, path, num_pics, google=False):
    filters = dict(type='photo')
    crw = GoogleImageCrawler(storage={"root_dir": path}) if google else BingImageCrawler(
        storage={"root_dir": path})
    crw.crawl(keyword=q, filters=filters, max_num=num_pics, overwrite=True)

