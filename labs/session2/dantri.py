# 1.1 open connection to page
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://dantri.com.vn"
conn = urlopen(url)

# 1.2 read data 
raw_data = conn.read()


# 1.3 decode data
html_page = raw_data.decode("utf-8")

# 1.4 save data to file
# 1.4.1 open connection to file
# 1.4.2 write data
# 1.4.3 close connection
# f_conn = open('dantri.html', 'wb')
# f_conn.write(raw_data)
# f_conn.close()

soup = BeautifulSoup(html_page, "html.parser")
ul = soup.find('ul', "ul1 ulnew")                       # id = "tbl_grade"

li_list = ul.find_all("li")
# print(li_list[0].prettify())
# for li in li_list:
#     print(li.prettify())
# li = li_list[0]

new_list = []

for li in li_list:
    a = li.h4.a
    title = a.string
    link = url + a["href"]
    news = {
        "Title": title,
        "Link": link,
    }
    new_list.append(news)
    # print(title)
    # print(link)
    # print("*"*10)
import pyexcel
pyexcel.save_as(records=new_list, dest_file_name="dantri.xlsx")
