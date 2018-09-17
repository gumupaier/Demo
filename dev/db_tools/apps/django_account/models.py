from django.db import models
from .helper import generate_id, get_time


# Create your models here.
class Account(models.Model):
    id = models.CharField(max_length=40, primary_key=True, default=generate_id)
    create_time = models.IntegerField("创建时间")
    name = models.CharField("姓名", max_length=40, default="")
    age = models.IntegerField("年龄")
    nick_name = models.CharField("花名", max_length=40, default="")
    class_name = models.CharField("班级名称", max_length=40, default="")
    mobile = models.CharField("手机号", max_length=20, default="", null=True)
    qq = models.CharField("QQ", max_length=20, default="", null=True)
    email = models.EmailField()

    class Meta:
        db_table = "account"


class MemberUserAccount(models.Model):
    id = models.CharField(max_length=40, primary_key=True, default=generate_id)
    password = models.CharField(max_length=128)
    salt = models.CharField(max_length=8)
    create_time = models.IntegerField(default=get_time)

    class Meta:
        db_table = "user_account"
