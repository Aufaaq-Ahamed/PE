import requests
import csv
from bs4 import BeautifulSoup

rows = []
while True:
    keyword = input("Enter the keyword, to exit press 'x'")
    if (keyword == 'x'): 
        break
    # keyword = "books"
    url = f"https://www.exportersindia.com/search.php?srch_catg_ty=prod&term={keyword}&cont=IN&ss_status=N"

    fields = ['Name', 'Address']

    data = requests.get(url=url)
    soup = BeautifulSoup(data.text, "html.parser")
    x = soup.find_all("li", class_="fo classified with_thumb big_text")
    for i in x:
        li = []
        y = i.find("a", class_="blue fw6 com_nam").string
        z = i.find_all("span")[-1].string
        li.append(y)
        li.append(z)
        rows.append(li)
    print(rows)

with open('data_content', 'w') as f:

    write = csv.writer(f)
        
    write.writerow(fields)
    write.writerows(rows)