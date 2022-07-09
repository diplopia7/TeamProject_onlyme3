from datetime import datetime

from django.db import models

# Create your models here.

# django 에서 폼 데이터를 다루는 방법은 크게 2가지 - Medel, MedelForm
# Member 테이블의 구조와 유사하게 member 모델 정리 - Model
class Member(models.Model):
    id=models.AutoField(primary_key=True)
    userid = models.CharField(max_length=18)
    passwd=models.CharField(max_length=18)
    name=models.CharField(max_length=5)
    jumin=models.CharField(max_length=13, default='')
    phone=models.CharField(max_length=11, default='')
    email=models.CharField(max_length=100)
    cash=models.IntegerField(default=0)
    regdate=models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'member'     # 생성할 테이블 이름 지정
        ordering = ['-regdate'] # 정렬기준 지정 최근가입일부터 정렬

    def __str__(self):
        return self.userid     # 객체 출력시 출력형태 정의