import selenium
from selenium import webdriver

def main():
    # Using Chrome to access web
    driver = webdriver.Chrome()
    # Open the website
    driver.get('https://canvas.case.edu')


if __name__ == '__main__':
    main()