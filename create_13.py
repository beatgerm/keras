import requests
from bs4 import BeautifulSoup

url = "https://bp.eosgo.io/listing/eos-cafe-calgary//"

def get_bp_info(url):
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")

    profile_name = bs_obj.find("div", {"class":"profile-name"})

    h1_bp_name = profile_name.find("h1")
    bp_name = h1_bp_name.text

    cover_buttons = bs_obj.find("div", {"class":"cover-buttons"})

    button_label = bs_obj.find("span", {"class":"button-label"})
    location = button_label.text
    print(location)

    lis = cover_buttons.findAll("li")
    li_tag = lis[1]

    a_tag = li_tag.find("a")
    link = a_tag['href']

    dictionary1 = {}
    dictionary1['name'] = bp_name
    dictionary1['location'] = location
    dictionary1['link'] = link

    return dictionary1

dic_result = get_bp_info(url)
print(dic_result)
