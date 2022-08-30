
# i have created by my Self/////////###########
from django.http import HttpResponse
from django.shortcuts import render  

def index (request):
    return render (request,'index2.html')
    # return HttpResponse ('''<h2>Ram is great</h2> <br>
    # <button onclick="http://127.0.0.1:8000/about/'">HTML Tutorial</button>
    # <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7" target="_blank"  style="width:42px;height:42px; color:green;" > <b>You Tube Django tutorial</b> </a><br><br><h2>shyam is great</h2>  <a href="https://www.w3schools.com/html/html_attributes.asp" target="_blank"  style="width:42px;height:42px; color:pink;" > <b>You Tube Django tutorial</b> </a>''')


def analyze(request): 
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps= request.POST.get('fullcaps', 'off')
    space= request.POST.get('space', 'off')
    newline= request.POST.get('newline', 'off')
    counter= request.POST.get('counter', 'off')
    print(djtext)
    print(removepunc)
    print(fullcaps)

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed

    if fullcaps=="on":
        analyzed =""
        for char in djtext:
               analyzed = analyzed + char.upper()
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed

    if space=="on":
        analyzed = ""
        for index, char  in enumerate (djtext):
            if not( djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed


    if newline=="on":
        analyzed = ""
        for char in djtext:
            if char != "/n ":
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed   
    
    if counter=="on":
        removespace1=djtext.replace(' ','')
        analyzed=len(removespace1)
        analyzed = len(djtext)
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        


    if (removepunc!= "on"and fullcaps!= "on"and space != "on"and newline != "on"and counter!="on"):
       
                      return HttpResponse("ERRORR")



    return render(request, 'analyze.html', params) 

   
