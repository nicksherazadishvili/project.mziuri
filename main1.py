website = requests.get("https://www.curseforge.com/skyrim/search?page=1&pageSize=50&sortType=3&class=mods", headers=headers).text
soup = BeautifulSoup(website, 'lxml')
mods = soup.find_all('li', class_= 'overlay-link')
c = 0

for mod in mods:
    Name = mods.find('h3', class_= 'ellipsis').text.split('. ')[1:]
    Name = "{}".format(*Name)