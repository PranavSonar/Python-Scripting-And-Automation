import requests
status=requests.get('https://github.com/vk04190/A-Professional-Responsive-Business-Website/blob/master/index.htmlsas')
print (status.raise_for_status())
print(status.text[:15])
for chunk in 