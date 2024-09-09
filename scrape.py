import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service 
import time
from bs4 import BeautifulSoup
def scrape_website(website):
    print("Launching Chrome Browser....")

    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver =  webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print('Page Loaded...')
        html = driver.page_source
        time.sleep(10)

        return html
    finally:
        driver.quit()

# Beutiful Soup is a HTML Parser
def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content  = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content (body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    #Looks inside the Parsed content and removes the script and style 
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    cleaned_content = soup.get_text(separator="\n")
    # Removes unneccesary Backslash n charracters
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
        )
    return cleaned_content

#Splitting the content up into Batches because LLM's have a Token limit which is about 8000 Characters

def split_dom_content(dom_content, max_lenght = 6000):
    return [
    dom_content[i : i + max_lenght] for i in range(0, len(dom_content), max_lenght)
    ]