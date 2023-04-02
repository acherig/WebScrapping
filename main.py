import requests
import selectorlib
import sqlite3

from datetime import datetime

URL = "https://programmer100.pythonanywhere.com/"

connection = sqlite3.connect("data.db")

def scrape(url):
    response = requests.get(url)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extraxt.yaml")
    value = extractor.extract(source)["tours"]
    return value

def store(extracted):
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    row = extracted.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperature VALUES(?,?)",  (now, extracted))
    connection.commit()


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
    store(extracted)