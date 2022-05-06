from django.shortcuts import render
from .models import *
import numpy as np
# Create your views here.
def home(request):
    return render(request,'home.html')

def news(request):

    query_string = request.GET.get("keyword")
    keyword = str(query_string)
    data = covid_news.objects.filter(content__contains=keyword)

    query_string2 = request.GET.get("tag_news")
    tag_news = str(query_string2)
    data2 = covid_news.objects.filter(tag_news__contains=tag_news)


    return render(request,'news.html', {'data':data,'data2':data2})



def post(request):
    id_news = int(request.GET.get('id_news'))
    data = covid_news.objects.get(id=id_news)

    id_recommend = np.random.randint(1, 101, 4)
    data_recommend = covid_news.objects.filter(id__in=id_recommend)


    return render(request,'post.html', {"data": data,"data_recommend":data_recommend})