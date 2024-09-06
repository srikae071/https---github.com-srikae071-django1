# my created file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # print(response.GET.get(text,default)

    return render(request, 'index.html')

def contacts(response):
    return HttpResponse('''<h1>knv fvuhu</h1><a href="https://www.olivaclinic.com/blog/laser-hair-removal-cost-in-bangalore/" aria-label="Show track">TOP QUESTIONS</a>' ''')

def analizeframefunc(request):
    # print(request.GET.get('text','default'))
    
    
    djtext=(request.GET.get('text','default'))


    orderpassed=request.GET.get('removepunc','off')
    print(djtext)
    print(orderpassed)
    puncuvations = '''!()-[];:'"\,<>./?@#$%^&* ~'''
    corctword=''
    if(orderpassed=='on'):
        for i in djtext:
            if( i not in puncuvations):
                corctword=corctword+i
    else:
         return HttpResponse('Error')
        
        
    # print(djtext)
    
    params={'analyzedcontent':'punch removed','ans':corctword}
    return render(request,'analizepage.html',params)
