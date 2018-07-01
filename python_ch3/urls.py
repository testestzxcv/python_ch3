"""python_ch3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# from emaillist import views
import emaillist.views as emaillist_views
import guestbook.views as guestbook_views

# url에 저장된 함수들이 실행된다.
# views 에 있는 함수를 실행
# path('들어갈 경로 이름',<- 적용할 함수 이름)
urlpatterns = [
    path('admin/', admin.site.urls),  # admin/ url로 들어온 내용으로 urls 함수를 실행.

    # path('emaillist/', emaillist_views.index),  # emillist/ url로 들어온 내용으로 index 함수를 실행.
    path('emaillist/', emaillist_views.test_index),  # emillist/ url로 들어온 내용으로 index 함수를 실행.
    path('emaillist/test_form', emaillist_views.test_form),
    # path('emaillist/test_index', emaillist_views.test_index),
    # path('emaillist/form', emaillist_views.form),  # emillist/form url로 들어온 내용으로 form 함수를 실행.
    # path('emaillist/add', emaillist_views.add),  # emillist/add url로 들어온 내용으로 add 함수를 실행.
    path('emaillist/add', emaillist_views.add),  # emillist/add url로 들어온 내용으로 add 함수를 실행.

    path('guestbook/', guestbook_views.index),  # guestbook/ url로 들어온 내용으로 index 함수를 실행.
    path('guestbook/add', guestbook_views.add),  # guestbook/add url로 들어온 내용으로 add 함수를 실행.
    # path('guestbook/deleteform', guestbook_views.delete),
]

