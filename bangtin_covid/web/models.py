from django.db import models

# Create your models here.
class covid_links_news(models.Model):
    link = models.CharField(max_length=500)
    tag_news = models.CharField(max_length=100, default="dantri.com.vn")
    def __str__(self):
        return self.link

class covid_news(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=5000)
    content = models.CharField(max_length=5000)
    keywords = models.CharField(max_length=5000)
    url_news = models.CharField(max_length=5000)
    url_img = models.CharField(max_length=5000)
    publish_date = models.CharField(max_length=5000)
    summarize_content = models.CharField(max_length=5000,null=True)
    tag_news = models.CharField(max_length=100,default="dantri.com.vn")
    def __str__(self):
        return self.title