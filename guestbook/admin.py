from django.contrib import admin
from guestbook.models import Guestbook

# Register your models here.
admin.site.register(Guestbook)  # 관리자 페이지에서 만든 모델을 보기위해 모델 등록