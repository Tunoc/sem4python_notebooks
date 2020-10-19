import bs4
from car import car
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class car_basen_dK():
    """
    Selenium webscraper.
    """

    def __init__(self):
        base_url = 'https://www.bilbasen.dk/'
        print("Setting up...")
        options = Options()
        options.headless = True
        print("Launching browser...")
        self.browser = webdriver.Firefox(options=options)
        print("Redirecting url to:", base_url)
        self.browser.get(base_url)
        self.browser.implicitly_wait(3)

    def clicker(self, click_this):
        try:
            click_this.click()
        except:
            # If we fail to click, it means the cokie accept/decline has loaded.
            try:
                accept_btn_cookies = self.browser.find_element_by_id(
                    "onetrust-accept-btn-handler")
                accept_btn_cookies.click()
                print("Cookie popup handled...")
                sleep(1)
                click_this.click()
            except:
                print('Error - Something went wrong when trying to click')
        # Wait for things to load after clicking.
        sleep(1)

    def no_leasing_search(self, search_car):
        # Find and uncheck the leasing label
        leasing_label_checkbox = self.browser.find_element_by_css_selector(
            "[data-track-action=\"leasing-toggle\"]")
        self.clicker(leasing_label_checkbox)

        # Find and write to the searchbar
        search_bar_element = self.browser.find_element_by_css_selector(
            "[placeholder=\"Søg på bil\"]")
        search_bar_element.send_keys(search_car)

        # Press the search button
        search_btn_element = self.browser.find_element_by_css_selector(
            ".btn.bb-btn-secondary.header-free-search-button")
        self.clicker(search_btn_element)
        print("Redirected url to:", self.browser.current_url)
        return self.browser.current_url

    def get_all_cars_info(self, search_url):
        self.browser.get(search_url)
        print("Fetching page content...")
        soup = bs4.BeautifulSoup(self.browser.page_source, "html.parser")
        select_colXS6 = soup.select(
            "#srp-content .row.listing.bb-listing-clickable > .col-xs-6")
        # Now we scraped all cars - We need to handle exclusive deals diffrently.
        # There are different amounts of divs with info in the Exclusive deals - rows
        filtered_colXS6 = filter(lambda x: len(
            x.select('.row')[0].find_all('div')) == 5, select_colXS6)
        car_links = soup.find_all('a', {'class': 'listing-heading darkLink'})
        cars = []
        for url, info_element in zip(car_links, filtered_colXS6):
            # Extract the url
            tmp_url = "https://www.bilbasen.dk" + url.get("href")
            # Extract the kilometers and price
            html_divs = info_element.select('.row')[0].find_all('div')
            tmp_km = html_divs[2].text
            tmp_price = html_divs[4].text.split(" ")[0]
            cars.append(car(tmp_url, tmp_price, tmp_km))
        print("Content sample:", cars[0])
        return cars

    def quitSelenium(self):
        """
        Quits selenium
        """
        print('- Quitting selenium')
        self.browser.quit()


if __name__ == "__main__":
    test = car_basen_dK()
    try:
        url_bentley = test.no_leasing_search("Mercedes")  # Bentley
        cars = test.get_all_cars_info(url_bentley)
        # print(len(cars))
        # for car in cars:
        #     print(car)
        cheapest_car_pr_km = car.cheapest_pr_km(cars)
        print(cheapest_car_pr_km)
        print("Succesfully completed")
    finally:
        test.quitSelenium()
