# from urllib.request import urlopen
# from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
# import regular expressions. comes standard with python as a module.
import re


def fetching_url():
    # create a new variable name
    # html = urlopen("http://shakespeare.mit.edu/lll/full.html")
    # bsobj = BeautifulSoup(html.read(), "html.parser")
    # print bsobj
    # parse url. use urllib/requests.fetching it

    # investigate the HTML page. Try to find what you might want to scrape
    # from an HTML page.
    # html = requests.get("http://shakespeare.mit.edu/lll/full.html")
    # print html.status_code  # if the webpage was downloaded successfully //
    # 200 is OK

    # use beautifulsoup and converts into XML. now a python object
    # bsobj = BeautifulSoup(html.content, "html.parser")
    # print bsobj.prettify() # will look beautiful
    # print bsobj.h3  # now an attribute of the object

    # how to get all the elements that start with an h3 tag?
    # two functions in BeautifulSoup =
    # findAll(tag(ex-h3, a, h1, p), attributes (color, attributes in html), recursive (how deep you want to go - nested elements), text(some text in particular), limit (how many), keywords (like text)) = will find all
    # find(tag, attributes, recursive, text, keywords) - will find one

    # create a list of all h3 tags
    # h3 = bsobj.findAll("h3")

    # iterate through list
    # for tag in h3:
    #     # print tag  # will print with html tags
    #     print tag.get_text()  # will print without html tags

    # nameList = bsobj.findAll(text="DUMAIN")
    # print nameList
    # print len(nameList)

    # Let us add another argument
    # new_object = bsobj.find("a", {"name": "1.1.9"})
    # print new_object.get_text()

    # Lets scrape another site
    html_page = requests.get("http://clickaces.com/contact/")
    # bsobj = BeautifulSoup(html_page.content, "html.parser")
    # print html_page.status_code
    bsobj = BeautifulSoup(html_page.content, "html.parser")
    # print bsobj.prettify()

    # bsobj_email = bsobj.findAll(text="info@clickaces.com")
    bsobj_emails = bsobj.findAll(text=re.compile(
        r"[A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)"))
    for email in bsobj_emails:
        print email
    print len(bsobj_emails)
    # print bsobj_email

    # Now how to scrape websites that use SSL
    # 1. tell them that you are a browser
    # 2. import the SSL module

fetching_url()
