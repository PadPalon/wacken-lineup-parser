from bs4 import BeautifulSoup

def read_html():
    with open("input.html", "r", encoding = "utf-8") as html:
        return BeautifulSoup(html.read(), features="html.parser")
    
def get_band(element, filter = lambda : True):
    base_element = element.contents[0].contents[1]
    band = base_element.contents[0].text.strip()
    info = base_element.contents[1].text.strip()
    if filter(info):
        return band
    else:
        return ""

def unique(list):
    set = []
    for value in list:
        if (value not in set):
            set.append(value)
    return set

nonsense = ["TBA"]
def not_nonsense(band):
    return band not in nonsense

def is_metal_battle(info):
    return info.startswith("MB")

def write_bands(elements, band_filter, filename):
    bands = [get_band(element, band_filter) for element in elements]
    bands = unique(bands)
    bands = sorted(bands)
    bands = filter(None, bands)
    bands = filter(not_nonsense, bands)
    bands = map(lambda band : band + "\n", bands)
    with open(filename, "w", encoding = "utf-8") as output:
        output.truncate(0)
        output.writelines(list(bands))

def write_regular(elements):
    write_bands(elements, lambda info : not is_metal_battle(info), "regular")

def write_metal_battle(elements):
    write_bands(elements, lambda info : is_metal_battle(info), "metal_battle")

html = read_html()
elements = html.select("div.event-list-item")
write_regular(elements)
write_metal_battle(elements)