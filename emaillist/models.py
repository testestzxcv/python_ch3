from django.db import models

# Create your models here.



# class Emaillist(models.Model):  # DB에 있는 이메일 리스트를 보여준다. CRUD 중에 CR만 있다.
#     first_name = models.CharField(max_length=50)   # varchar에 max length 값 주기.
#     last_name = models.CharField(max_length=100)
#     email = models.CharField(max_length=200)
#
#     def __str__(self):  # 자바의 toString() 함수와 비슷하다.
#         return 'Emaillist(%s, %s, %s)' % (self.first_name, self.last_name, self.email)


class Emaillist(models.Model):  # DB에 있는 이메일 리스트를 보여준다. CRUD 중에 CR만 있다.
    first_name = models.CharField(max_length=50)   # varchar에 max length 값 주기.
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)

    def __str__(self):  # 자바의 toString() 함수와 비슷하다.
        return 'Emaillist(%s, %s, %s)' % (self.first_name, self.last_name, self.email)
