import bs4
import requests


def get_amajon(producturl):
    content = requests.get(producturl)
    content.raise_for_status()
    # print(content.status_code)
    # print(content.headers)
    # print(content.headers['Server'])
    # print(content.text)
    # print(content.json())
    fmt_content = bs4.BeautifulSoup(content.text, "html.parser")
    selected_content = fmt_content.select('#sort-menu')
    # print(selected_content.text)

prince=get_amajon('https://www.youtube.com/watch?v=wtR8sH3fLO8')
# print('The Price is '+prince)
