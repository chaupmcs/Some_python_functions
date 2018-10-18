from bs4 import BeautifulSoup
import urllib.request as urllib
import json

def scraping_data(url, prefix):

    req = urllib.Request(url, headers={'User-Agent': "Magic Browser"})
    r = urllib.urlopen(req).read()
    soup = BeautifulSoup(r, "lxml")

    letters = soup.find_all("div", class_="ec_statements")

    #create an empty dictionary to store data
    lobbying = {}
    for element in letters:
        lobbying[element.a.get_text()] = {}

    #get url link
    for element in letters:
        lobbying[element.a.get_text()]["link"] = prefix + element.a["href"]

    for element in letters:
        lobbying[element.a.get_text()]["date"] = element.find('div',id="legalert_date").get_text()
    return lobbying


def print_out(lobbying):
    for item in lobbying.keys():
        print(item + ": " + "\n\t" + "link: " + lobbying[item]["link"] + "\n\t" + "date: " + lobbying[item]["date"] + "\n\n")

def write_file(lobbying):
    with open("lobbying.json", "w") as writeJSON:
        json.dump(lobbying, writeJSON)

if __name__ == '__main__':
    lobbying = scraping_data('http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts', "www.aflcio.org")
    print_out(lobbying)
    write_file(lobbying)


