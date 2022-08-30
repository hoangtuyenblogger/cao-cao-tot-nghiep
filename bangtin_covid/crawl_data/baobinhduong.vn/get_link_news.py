from bs4 import BeautifulSoup
import requests
import sqlite3

def get_link_news_by_page(url):
    #url ="https://baobinhduong.vn/toan-canh-covid-19/toan-dan-chong-dich/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    news_block = soup.findAll('div', class_="left borderbottomdotted paddingbottom5 paddingtop10")
    link_news = [div.find('a').attrs['href'] for div in news_block]
    return link_news

def add_data(data):
    conn = sqlite3.connect(r"D:\Dai Hoc Thu Dau Mot\Nam 4\HK II\Doantotnghiep\bangtin_covid\db.sqlite3")
    query = "INSERT INTO web_covid_links_news(link,tag_news) VALUES (?,?)"
    tag_news = "baobinhduong.vn"
    for link in data:
        conn.execute(query, (link,tag_news))
        conn.commit()
        print("added to database ", link)

if __name__ == '__main__':

    page_start = input("Nhập page bắt đầu cần get: ")
    page_end = input("Cho đến page: ")
    for page in range(int(page_start),int(page_end)+1):
        url = "https://baobinhduong.vn/toan-canh-covid-19/toan-dan-chong-dich/?p={}".format(str(page))
        print("Root url: ",url )
        print("====================================================================================")
        try:
            data = get_link_news_by_page(url)
            add_data(data)
        except Exception as erro:
            print("Đã có lỗi: ", erro)
            pass


