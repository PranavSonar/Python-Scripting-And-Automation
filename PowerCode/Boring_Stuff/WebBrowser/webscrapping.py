import bs4,requests

get_page=requests.get('https://www.youtube.com/watch?v=R8rNw0bGOBA&list=RDR8rNw0bGOBA&start_radio=1')
status=get_page.raise_for_status()
# print(status)
shoup=bs4.BeautifulSoup(get_page.text,'html.parser')
print(shoup)
 

 