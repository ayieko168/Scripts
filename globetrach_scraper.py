
from turtle import ht
import pandas as pd
import concurrent.futures
import time
from requests_html import HTMLSession, user_agent

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

EXCEL_FILE = "D:\Downloads/KHRC EDITORIAL REPORT  SEPTEMBER 2022.xlsx"

def get_list_of_links():
    
    print(f"\n\nGetting the links from the excel file: {EXCEL_FILE} ...")

    xls_file = pd.ExcelFile(EXCEL_FILE)
    sheet_names = [sheet for sheet in xls_file.sheet_names]

    links_list = []
    for sheet in sheet_names:
        df = pd.read_excel(EXCEL_FILE, sheet_name=sheet_names[2])
        links_df = df.iloc[:,18:].dropna().values.tolist()
        l = [item for sublist in links_df for item in sublist]
        links_list += l

    print(f"Found {len(links_list)} links in the file: {EXCEL_FILE}")
    return links_list

def scrape_and_download_link(session, url):
    
    try:

        options = webdriver.ChromeOptions()
        options.add_argument(r"--user-data-dir=C:\Users\RoyalState\AppData\Local\Google\Chrome\User Data") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
        options.add_argument(r'--profile-directory=C:\Users\RoyalState\AppData\Local\Google\Chrome\User Data\Profile 1') #e.g. Profile 3

        driver = webdriver.Chrome(executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe", chrome_options=options)
        driver.get(url)

        html = driver.page_source

        elem = driver.find_element(By.CLASS_NAME, "btn-primary")
        print(elem)
        # time.sleep(2)
        # print(html)

        driver.close()

    except Exception as e:
        print(f"Error scraping and downloading the link {url}. Exception: {e}")
        return
    


def main():

    # links_list = get_list_of_links()

    session = HTMLSession()
    scrape_and_download_link(session, "https://portal.globetrack.co.ke/MyMonitoredEntries/62bb14f3-8b32-48b6-b654-ee54a7226d17")



main()

