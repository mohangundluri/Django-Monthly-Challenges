from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

month_text = {
    "jan": "This is jan",
    "feb": "This is feb",
    "mar": "This is march",
    "apr": "This is april",
    "may": "This is may",
    "june": "This is June",
    "july":"This is July",
    "aug":None,
}


def home(request):
    months = list(month_text.keys())
    return render(request, "challenges/home.html", {'months':months})


def month_text_by_str(request, month_name):
    try:
        text = month_text[month_name]
        return render(request, 'challenges/challenges.html', {"month_name":month_name.capitalize(),
                                                              "text":text})
    except:
        raise Http404()

def month_text_by_number(request, month_number):
    months = list(month_text.keys())
    if month_number > len(months):
        return HttpResponse("Index is large")
  
    redirect_month = months[month_number-1]
    redirect_path = reverse('challege_by_str', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)