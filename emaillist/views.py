from django.shortcuts import render
# from emaillist.models import Emaillist
from emaillist.models import Emaillist
from django.http import HttpResponseRedirect

# Create your views here.

# def index(request):
#     emaillist_list = Emaillist.objects.all().order_by('-id')    # db에서 objects 전체를 불러와서 변수에 저장
#     data = {'emaillist_list':emaillist_list}    # 딕션너리 형식으로 데이터에 저장
#     return render(request, 'emaillist/index.html', data)    # render 라는 임시변수에 url(request)에서 불러온 값으로 emillist/index.html 형식으로 data값을 출력한다.


def test_index(request):
    print("test_index 함수 실행하자 ")
    emaillist_list = Emaillist.objects.all().order_by('-id')    # db에서 objects 전체를 불러와서 변수에 저장
    data = {'emaillist_list':emaillist_list}    # 딕션너리 형식으로 데이터에 저장
    return render(request, 'emaillist/test_index.html', data)

# def form(request):
#     return render(request, 'emaillist/form.html')

def test_form(request):
    print("test 함수 실행하자 ")
    return render(request, 'emaillist/test_form.html')


def add(request):
    emaillist = Emaillist()
    emaillist.first_name = request.POST['fn']   # 웹에 first_name부분에 작성한 값 (index.html에서 input으로 받은 password) 을 가져와서 데이터베이스(emailist)의 first_name column에 저장
    emaillist.last_name = request.POST['ln']   # 웹에 last_name부분에 작성한 값 (index.html에서 input으로 받은 password) 을 가져와서 데이터베이스(emailist)의 last_name column에 저장
    emaillist.email = request.POST['email']   # 웹에 email부분에 작성한 값 (index.html에서 input으로 받은 password) 을 가져와서 데이터베이스(emailist)의 email column에 저장

    emaillist.save()    # 저장된 내역을 DB에 저장

    return HttpResponseRedirect('/emaillist')   # 저장완료되면 기존 리스트 페이지로 이동
#
# def add2(request):
#     emaillist2 = Emaillist2()
#     emaillist2.first_name = request.POST['fn']
#     emaillist2.last_name = request.POST['ln']
#     emaillist2.email = request.POST['email']
#
#     emaillist2.save()
#
#     return HttpResponseRedirect('/emaillist')