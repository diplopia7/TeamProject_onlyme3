from django.db import models
from member.models import Member


# Create your models here.
class Shop(models.Model):
    id = models.AutoField(primary_key=True)
    cname = models.TextField()
    img = models.TextField(default='')
    innertrait = models.TextField()
    fighttrait = models.TextField()
    skill = models.TextField()
    price=models.IntegerField(default=0)

    class Meta:
        db_table = 'shop'     # 생성할 테이블 이름 지정
        ordering = ['cname']

    def __str__(self):
        return self.cname     # 객체 출력시 출력형태 정의


class Possession(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Member, on_delete=models.DO_NOTHING)
    cname = models.ForeignKey(Shop, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'possession'     # 생성할 테이블 이름 지정
        ordering = ['id']

    def __str__(self):
        return self.userid     # 객체 출력시 출력형태 정의