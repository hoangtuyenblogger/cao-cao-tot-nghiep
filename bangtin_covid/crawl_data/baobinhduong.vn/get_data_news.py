from newspaper import Article
import re
import warnings
import sqlite3
import requests
from bs4 import BeautifulSoup
from gensim.summarization import keywords as get_keywords
from gensim.summarization import summarize
from newspaper import Article
from pyvi.ViTokenizer import tokenize

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
#url = "https://dantri.com.vn/xa-hoi/thu-tuong-yeu-cau-tiep-tuc-kiem-soat-nguoi-ra-vao-tphcm-20210930183408003.htm"

def text_prossesing(text):
    text = re.sub(r'\s\s+', ' ', text.strip())
    # load stopword
    stopwords_vietnam = []
    with open('stopword_vietnam.txt', 'r', encoding="utf8") as f:
        for line in f:
            stopwords_vietnam.append(line.strip())
    # lowercase
    text = text.lower()
    # remove tags
    text = re.sub("&lt;/?.*?&gt;", " &lt;&gt; ", text)
    # remove stopword
    text = ' '.join([word for word in text.split() if word not in stopwords_vietnam])
    text = tokenize(text)
    return text

def extract_data(text, ratio=0.2):
    text = text_prossesing(text)
    return summarize(text, ratio=0.2), get_keywords(text, ratio=0.2)


'''conn = sqlite3.connect("data.db")
query ='INSERT INTO data_news (title,description,content,keywords,url_news,url_img) VALUES (?,?,?,?,?,?)'
conn.execute(query, (article.title,article.meta_description,article.text,keywords,article.url,article.top_img))
conn.commit()
print("Done ",url)'''

def get_data_news(url, tag_news, conn):
    try:
        article = Article(url)
        article.download()
        article.parse()

        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        title = article.title # ok

        text_element = soup.find('div', id='newscontents')
        text_in_p = [str(p.text).strip() for p in text_element.findAll('p')]
        text = " ".join([word for word in text_in_p])  # ok
        text = text_prossesing(text)  # ok

        img = article.top_img # ok

        # get keywword
        category_element = soup.find('div', class_="block_tag marginbottom10")
        keyword = [str(a.text).strip() for a in category_element.findAll('a')]
        keywords = "|".join([word for word in keyword]) # ok

        # get meta_des
        meta_element = soup.findAll('meta')
        meta_description = str(meta_element[2].attrs['content'])

        # get public_time
        public_date = soup.find('div', class_="ngaycapnhat").text.replace("Cập nhật: ","").strip().replace(" ","") #ok

        # summarize(text, ratio=0.2)
        summarize_content = summarize(text, ratio=0.2)

        # conn = sqlite3.connect("data.db")
        query = """INSERT INTO web_covid_news (title, description,content, keywords,url_news, url_img,publish_date, summarize_content, tag_news) 
            VALUES (?,?,?,?,?,?,?,?,?)"""
        conn.execute(query, (title, meta_description, text, keywords, url, img, public_date, summarize_content,tag_news))
        conn.commit()
        print("Done ", url)
    except Exception as erro:
        print(print("Đã có lỗi:", erro))
        pass


if __name__ == '__main__':

    conn = sqlite3.connect(r"D:\Dai Hoc Thu Dau Mot\Nam 4\HK II\Doantotnghiep\bangtin_covid\db.sqlite3")
    try:
        print("######## Cào dữ liệu theo thứ tự ID bài báo")
        start = int(input("Bắt đầu từ: "))
        end = int(input("Đến: "))
        link_news = conn.execute("SELECT id, link, tag_news FROM web_covid_links_news where id BETWEEN ? AND ?", (start, end))

        for row in link_news:
            #print(row[1],row[2])
            get_data_news(row[1],row[2], conn)
    except Exception as erro:
        print("Đã có lỗi:", erro)
        pass



