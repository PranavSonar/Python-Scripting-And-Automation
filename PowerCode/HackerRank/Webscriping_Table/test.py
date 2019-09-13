# to get data from webpages
import requests
# to parse data
from bs4 import BeautifulSoup as bsp

# url=r'https://www.copart.com/vehicleFinderSearch/?displayStr=%5B2009%20TO%202020%5D&searchStr=%7B%22MISC%22:%5B%22%23VehicleTypeCode:VEHTYPE_V%22,%22%23LotYear:%5B2009%20TO%202020%5D%22%5D,%22sortByZip%22:false,%22buyerEnteredZip%22:null%7D'
# url=r'https://www.copart.com/vehicleFinderSearch/?displayStr=%5B2009%20TO%202020%5D&searchStr=%7B%22MISC%22:%5B%22%23VehicleTypeCode:VEHTYPE_V%22,%22%23LotYear:%5B2009%20TO%202020%5D%22%5D,%22sortByZip%22:false,%22buyerEnteredZip%22:null%7D'
# url='https://www.copart.com/auctionCalendar/'
url='https://www.copart.com/lot/22075808/Photos'
# to get content of web in a variable
response=requests.get(url)

bspcontent=bsp(response.content,'html.parser')
# find_content=bspcontent.find_all('div',class_='grid-col span-md-12 span-lg-10')
find_content=bspcontent.find_all('table',id='pokedex')

print(bspcontent)