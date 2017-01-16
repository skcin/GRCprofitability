import urllib.request
from bs4 import BeautifulSoup


requestUrl="http://wuprop.boinc-af.org/results/credit.py?fabricant=Intel&type=Core+i7&modele=i7-3770+%28HT+enabled%29&plateforme=all&tri=projet&sort=asc"
timeout=1
try:
    with urllib.request.urlopen(urllib.request.Request(requestUrl),timeout=timeout) as ret:
        res = ret.read().decode('utf-8')
except:
    res = None


soup = BeautifulSoup(res,"html.parser")
table = soup.find("table", attrs={"class":"bordered"})


headings_platform = [th.get_text() for th in table.find_all("tr")[1].find_all("th")]

headings=["Project","Application"]
for hp in headings_platform:
    headings.append(hp)

datasets = []
for row in table.find_all("tr"):
    if not row.find_all("th"):
        dataset={}
        idx=0
        for td in row.find_all("td"):
            if idx == 0:
                if td.has_attr('rowspan'):
                    CurrProject = td.get_text()
                else:
                    dataset[headings[idx]] = CurrProject
                    idx = 1
            dataset[headings[idx]] = td.get_text()
            idx += 1
        datasets.append(dataset)

