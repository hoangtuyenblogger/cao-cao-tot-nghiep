from bs4 import BeautifulSoup
import requests
import sqlite3


def get_link_news_by_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    news_block = soup.find('article', class_="article article-three large")
    news_element = news_block.findAll('h3', class_="article-title")
    link_news = [h3.find('a').attrs['href'] for h3 in news_element]
    return link_news


def add_data(data): #data là list chứa link vd: /suc-khoe/dai-dich-covid-19/3-9-2021.htm
    conn = sqlite3.connect("data.db")
    query = "INSERT INTO links_news(link) VALUES (?)"
    for link in data:
        full_link = "https://dantri.com.vn/" +link
        conn.execute(query, (full_link,))
        conn.commit()
        print("added to database ", full_link)

def get_news_per_day(): # mỗi ngày get 2 page = 30 bài báo
    for page in range(1,3):
        url = "https://dantri.com.vn/suc-khoe/vac-xin-covid-19/trang-{}.htm".format(str(page))
        print("Root url: ",url )
        print("====================================================================================")
        try:
            data = get_link_news_by_page(url)
            add_data(data)
        except Exception as erro:
            print("Đã có lỗi: ", erro)
            pass

if __name__ == '__main__':
    page_start = input("Nhập page bắt đầu cần get: ")
    page_end = input("Cho đến page: ")

    for page in range(int(page_start),int(page_end)+1):
        url = "https://dantri.com.vn/suc-khoe/vac-xin-covid-19/trang-{}.htm".format(str(page))
        print("Root url: ",url )
        print("====================================================================================")
        try:
            data = get_link_news_by_page(url)
            add_data(data)
        except Exception as erro:
            print("Đã có lỗi: ", erro)
            pass
