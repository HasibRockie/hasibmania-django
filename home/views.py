from django.shortcuts import render
from home.models import Post,Gratitude
from django.template import RequestContext

# Create your views here.
def index(request):
    all_posts = Post.objects.order_by('date').reverse()
    post_dic = { 'posts' : all_posts[:10]}
    return render(request, 'home/index.html',context=post_dic)

def allposts(request):
    all_posts = Post.objects.order_by('date').reverse()
    post_dic = { 'posts' : all_posts}
    return render(request, 'home/posts.html',context=post_dic)

def personals(request):
    personal_posts = Post.objects.filter(category='ব্যক্তিগত')
    post_dic = { 'posts' : personal_posts[::-1]}
    return render(request, 'home/personals.html',context=post_dic)

def religious(request):
    religous_posts = Post.objects.filter(category='ধর্মীয়')
    post_dic = { 'posts' : religous_posts[::-1]}
    return render(request, 'home/religious.html',context=post_dic)

def fictions(request):
    fictional_posts = Post.objects.filter(category='ফিকশন')
    post_dic = { 'posts' : fictional_posts[::-1]}
    return render(request, 'home/fictions.html',context=post_dic)

def gratitude(request):
    grat_dict = { 'dedicated' : Gratitude.objects.all()}
    return render(request, 'home/gratitude.html', context=grat_dict)

def post(request,id):
    post = Post.objects.get(id=id)
    # print(post)
    # print(Post.objects.all())
    print(len(Post.objects.all()))
    context = {'post': post}
    # if id > len(Post.objects.all()):
    return render(request, 'home/viewpost.html', context)
    # else:
        # return render(request,'home/not-found.html',context)

def errorhandler(request,exception):
    return render(request, 'home/not-found.html')




