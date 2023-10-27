from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest


# Create your views here.

def near_hundred(request:HttpRequest,n) -> HttpResponse:
    return HttpResponse(abs(n) < 100 and abs(n) >= 90 or abs(n) < 200 and abs(n) >= 190)

def stringsplode(request:HttpRequest,s) -> HttpResponse:
    result = ""
                                                   
    for i in range(len(s)):
        result = result + s[:i + 1]
    return HttpResponse(result)

def catdog(request:HttpRequest,cd) -> HttpResponse:
    count1 = 0
    count2 = 0
   
    if 'dog' and 'cat' not in cd:
        return True
    for i in range(len(cd)-1):
        if cd[i:i+3] == 'cat':
            count1 += 1
        if cd[i:i+3] == 'dog':
            count2 += 1
    if count1 == count2:
        return HttpResponse(True)
    else:
        return HttpResponse(False   )

def lone(request:HttpRequest,a,b,c) -> HttpResponse:
    sum = 0;
    if(a != b and a != c):
        sum += a;       
    if(b != a and b != c):
        sum += b;                  
    if(c != a and c != b):
        sum += c;
    
    return HttpResponse(sum)