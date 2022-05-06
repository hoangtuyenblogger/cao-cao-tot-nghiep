from django.contrib import admin

# Register your models here.
from .models import  covid_links_news , covid_news
admin.site.register(covid_links_news)
admin.site.register(covid_news)