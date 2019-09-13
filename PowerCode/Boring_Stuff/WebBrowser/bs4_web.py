import bs4
import requests
res=requests.get("https://www.amazon.in/b?node=16289319031&pf_rd_p=3b95b78c-ce44-4b75-a300-57f18b817847&pf_rd_r=HR8RCZ4Z1WW1N3RQR94G")
status=res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,"html.parser")