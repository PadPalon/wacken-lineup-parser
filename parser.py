from bs4 import BeautifulSoup

def read_html():
    with open("input.html", "r", encoding = "utf-8") as html:
        return BeautifulSoup(html.read(), features="html.parser")


html = read_html()
elements = html.select("h5.card-title.text-center")
with open("output", "w", encoding = "utf-8") as output:
    output.truncate(0)
    output.writelines("%s\n" % element.text for element in elements)