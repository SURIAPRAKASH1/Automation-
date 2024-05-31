from django.shortcuts import render
from .bot import selenium_script


def home_page(request):

    if request.method == 'POST':
       
        username = request.POST.get('username')
        password = request.POST.get('password')
        custom_input = request.POST.get('custom_input')

        selenium_script(username,password,custom_input)


    return render(request,'index.html')



    




