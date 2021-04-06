from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    counter = request.POST.get('counter', 'off')
    try:
        if removepunc == "on":
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            analyzed = ""
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char
            params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
            djtext=analyzed

            #return render(request, 'analyze.html', params)

        if fullcaps=="on":
            analyzed = ""
            for char in djtext:
                analyzed = analyzed + char.upper()

            params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
            djtext=analyzed
            # Analyze the text
            #return render(request, 'analyze.html', params)

        if extraspaceremover=="on":
            analyzed = ""
            for index, char in enumerate(djtext):
                if not(djtext[index] == " " and djtext[index+1]==" "):
                    analyzed = analyzed + char

            params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
            djtext=analyzed
            # Analyze the text
            #return render(request, 'analyze.html', params)

        if newlineremover == "on":
            analyzed = ""
            for char in djtext:
                if char != "\n" and char != "\r":
                    analyzed = analyzed + char

            params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
            djtext=analyzed
            # Analyze the text
            #return render(request, 'analyze.html', params)
        
        if counter == "on":
            count = 0
            for char in djtext:
                if not char == " ":
                    count = count + 1
            
            params = {'purpose': 'Counted characters:', 'analyzed_text': count}
            #djtext=analyzed 
        
        if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and counter != "on"):
            return HttpResponse("please select any operation and try again")

        return render(request, 'analyze.html', params)

    except:
        return HttpResponse( "Error" )