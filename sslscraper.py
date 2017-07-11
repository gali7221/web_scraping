import requests
import urllib
from bs4 import BeautifulSoup
import re
import csv


def table_to_csv():
    table_page = requests.get(
        "http://www.cmegroup.com/trading/equity-index/us-index/e-mini-sandp500.html", headers - {"User-Agent": "Mozilla/5.0"})

    # urllib.urlopen(table_page)
    result = urllib.request.urlopen(table_page)
    bsobj = BeautifulSoup(result, "html.parser")
    table = bsobj.find("table", {"id": "quotesFuturesProductTable1"})

    # creates a csv file, not read but write into file for 'wt'
    csvFile = open("sp_h.csv", "wt")
    writer = csv.writer(csvFile)  # csv module will help to write

    rows = table.findAll("tr")  # columns/rows
    # print rows

    for row in rows:  # iterate over 2-d list
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())  # append to list

        writer.writerow(csvRow)  # write into csv file


table_to_csv()


# For HW - go through Code and investigate line by line which will make
# much more sense.
