from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':'CoreyMS',
        'title':'Blog post 1',
        'content':'first post content',
        'date_posted':' august 27 , 2018'
    },
    {
        'author':'jane doe',
        'title':'Blog post 2',
        'content':'2 post content',
        'date_posted':' august 2 , 2012'
    }
]

def home(request):
    #create a dictionary 
    context = {
        'posts':posts #assign the key the dict posts
    }
    return render(request,'blog/home.html' ,context)


def about(request):
    return render(request,'blog/about.html',{'title':'jlo'})
