from selenium import webdriver

url = "https://youtube.com"

def get_views(count=20, video_link=url):
    """
    :param count: The number of views you want
    :return: None
    This function gets you views on youtube
    """

    driver = webdriver.Firefox()
    driver.get(url)



get_views()