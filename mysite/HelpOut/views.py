from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

from HelpOut.forms import RequestForm
from HelpOut.models import helpRequest


def index(request):
    return render(request, 'HelpOut/index.html')

def get_post(request):
    # if this is a POST request we need to process the form data
    request=request
    newRequest= helpRequest()

    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            newRequest.requestText=form.cleaned_data['your_request'] #Set the newComment's comment field to equal the input from the user
            newRequest.save() #Save that input to the database
            output = ', '.join([c.requestText for c in helpRequest.objects.all()])
            #return showAllComments(output)
            return render(request, 'HelpOut/requestslist.html', {
                'latest_comment_list' : helpRequest.objects.all()
            })

    else:
        form = RequestForm()

    return render(request, 'HelpOut/request.html', {'form': form})

def getAllRequests(request):
    return render(request, 'HelpOut/requestslist.html', {
        'latest_comment_list': helpRequest.objects.all()
    })