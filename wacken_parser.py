from bs4 import BeautifulSoup

def read_html():
    with open("input.html", "r", encoding = "utf-8") as html:
        return BeautifulSoup(html.read(), features="html.parser")
    
def get_band(element, filter = lambda : True):
    base_element = element.contents[0].contents[1]
    band = base_element.contents[0].text.strip()
    info = base_element.contents[1].text.strip()
    if filter(info):
        return (band, info)
    else:
        return None

def unique(list):
    set = []
    for value in list:
        if (value not in set):
            set.append(value)
    return set

nonsense = ["TBA"]
def not_nonsense(band):
    return band[0] not in nonsense

def is_metal_battle(info):
    return info.startswith("MB")

def concat_band_info(band):
    if (band[1] != ""):
        return band[0] + " (" + band[1] + ")" + "\n"
    else:
        return band[0] + "\n"

def write_bands(elements, band_filter, filename):
    bands = [get_band(element, band_filter) for element in elements]
    bands = filter(None, bands)
    bands = unique(bands)
    bands = sorted(bands, key=lambda band: band[1])
    bands = filter(not_nonsense, bands)
    bands = map(concat_band_info, bands)
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