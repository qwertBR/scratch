from selenium import webdriver
import requests
import time
import os
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


def get_information_by_url(name, url):
    time.sleep(1)
    try:
        os.mkdir(name)
    except FileExistsError:
        pass
    driver = webdriver.Chrome()
    driver.get(url)
    print("lol")
    images = driver.find_elements_by_class_name("magnifier-image")
    for img in images:
        el = img.get_attribute("src")
        response = requests.get(str(el))
        file = open(name + "/" + "sample_image.png", "wb")
        file.write(response.content)
        file.close()
    price_all = driver.find_elements_by_class_name("product-price-value")
    file = open(name + "/" + "price.txt", "w")
    i = 0
    for price in price_all:
        price = price.text
        file.write(str(price) + "\n")
        i += 1
    if i == 2:
        mark = driver.find_element_by_class_name("product-price-mark")
        file.write(str(mark.text))
        try:
            os.rename(name, "sale_" + name)
        except OSError:
            pass
    file.close()
    title = driver.find_element_by_class_name("product-title-text")
    file = open(name + "/" + 'title.txt', "w")
    file.write(str(title.text))
    file.close()


def get_products_from_category(category_name, category_url):
    time.sleep(1)
    try:
        os.mkdir(category_name)
    except FileExistsError:
        pass

    opts = Options()
    opts.add_argument("user-agent=" + str(UserAgent().Chrome))

    driver = webdriver.Chrome(chrome_options=opts)

    driver.get(category_url)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    urls = driver.find_elements_by_class_name("item-title")
    for el in urls:
        print(el.get_attribute("href"))


get_information_by_url('bankds',
                           "https://aliexpress.ru/af/category/202000543.html?categoryBrowse=y&origin=n&CatId=202000543&spm=a2g0o.best.110.4.ae905430ZB9YVo&catName=mp3-player&_ga=2.66095654.942602761.1609530161-532338886.1605034617")
