import os
import re

import dateparser
from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from web_scrapping.models import Web


class Command(BaseCommand):
    def handle(self, *args, **options):
        urls = ["https://galicjaexpress.pl/ford-c-max-jaki-silnik-benzynowy-wybrac-aby-zaoszczedzic-na-paliwie",
                "https://galicjaexpress.pl/bmw-e9-30-cs-szczegolowe-informacje-o-osiagach-i-historii-modelu",
                "https://take-group.github.io/example-blog-without-ssr/jak-kroic-piers-z-kurczaka-aby-uniknac-suchych-kawalkow-miesa",
                "https://take-group.github.io/example-blog-without-ssr/co-mozna-zrobic-ze-schabu-oprocz-kotletow-5-zaskakujacych-przepisow"]
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Remote(
            command_executor=os.getenv("SELENIUM_REMOTE_URL"),
            options=chrome_options
        )
        try:
            for number, url in enumerate(urls):
                print(f"Parsing: {number + 1}/{len(urls)}")
                driver.get(url)
                driver.implicitly_wait(30)
                pattern = r'\b\d{1,2}\.\d{1,2}\.\d{4}\b|' \
                          r'\b\d{1,2}\s+[a-ząćęłńóśźż]+\s+\d{4}\b|' \
                          r'\b\d+\s+(?:dni|tygodnie|miesiące|lata)\s+temu\b'

                title = driver.title
                content = driver.find_element(by=By.XPATH, value="//article")
                current_url = driver.current_url
                html_content = content.get_attribute("innerHTML")
                matches = re.findall(pattern, content.text, re.IGNORECASE)
                parsed = dateparser.parse(matches[0], languages=["pl"])
                if Web.objects.filter(url=url).exists():
                    continue
                else:
                    Web.objects.create(article_name=title, original_content=html_content, text_content=content.text,
                                       url=current_url, date=parsed)
        except TimeoutException:
            print("Timeout exception")
        driver.quit()
        print("Parsing complete!")
