from django.shortcuts import render
from django.http import HttpResponseRedirect
from guestbook.models import Guestbook

# Create your views here.

def deleteform(request):
    id = request.GET.get('id', False)
    context = {'id':id}
    return render(request)

# def delete(request):
#     Guestbook.objects.filter(id=10).filter(password=).delete()

def index(request):
    guestbook_list = Guestbook.objects.all().order_by('-regdate')    # db에서 objects 전체를 불러와서 변수에 저장

    context = {'guestbook_list': guestbook_list}    # 딕션너리 형식으로 데이터에 저장
    return render(request, 'guestbook/index.html', context)    # render 라는 임시변수에 url(request)에서 불러온 값으로 emillist/index.html 형식으로 context값을 출력한다.

def add(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']   # index.html 에 저장된 이름 사용
    guestbook.password = request.POST['password']   # 웹에 password부분에 작성한 값 (index.html에서 input으로 받은 password) 을 가져와서 데이터베이스(guestbook)의 password column에 저장
    guestbook.message = request.POST['message']   # 웹에 message부분에 작성한 값 (index.html에서 input으로 받은 message) 을 가져와서 데이터베이스(guestbook)의 password column에 저장

    guestbook.save()    # 저장된 내역을 DB에 저장

    return HttpResponseRedirect('/guestbook')   # 저장완료되면 기존 리스트 페이지로 이동



