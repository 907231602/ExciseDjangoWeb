from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'learn.html')

def base(request):
    return render(request, 'base.html')


def showString(request):
    string='我是中国人'
    return render(request, 'tmUP.html',{'string':string})

def forList(request):
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(request, 'forlist.html', {'TutorialList': TutorialList})

def showDict(request):
    info_dict = {'site': 'China', 'content': 'IT very best'}
    return render(request, 'showdict.html', {'info_dict': info_dict})

def ifFor(request):
    List = map(str, range(100))# 一个长度为100的 List
    return render(request, 'iffor.html', {'List': List})
