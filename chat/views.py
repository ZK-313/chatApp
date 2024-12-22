# from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader

# # Create your views here.
# def index(request):
#     template = loader.get_template('test.html')
#     return HttpResponse(template.render())
from django.shortcuts import render

def chat_room(request, room_name):
    current_user = request.user
    context = {
        'user': current_user,
    }
    return render(request, 'chat.html', {'room_name': room_name})
def chat(request):
    return render(request, 'chat.html')

