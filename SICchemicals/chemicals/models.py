from django.db import models

# Create your models here# .


class Author(models.Model):  # 继承于models.Model这个父类,从而实现多态
    first_name = models.CharField(max_length=32)  # 名字的字段,使用字符串格式,最大长度32
    last_name = models.CharField(max_length=32)
    email = models.EmailField()  # email字段,使用email自带的格式


class Chemical(models.Model):
    CAS = models.CharField(max_length=32)
    chinese_name = models.CharField(max_length=32)
    english_name = models.CharField(max_length=32)
    size = models.CharField(max_length=32)
    num = models.IntegerField()
    location = models.CharField(max_length=32)
    goumairen = models.CharField(max_length=32)
    shenpiren = models.CharField(max_length=32)
    rukutime = models.DateField()
    note = models.TextField(max_length=1000)

    def __str__(self):
        return self.chinese_name+self.english_name





class Person(models.Model):
    name = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)

    def __unicode__(self):  # 定义unicode函数,是为了让对象在实例化的时候,可以返回打印输出它的名字<阿文>.不至于显示为<** object>
        return self.name


class Chemicals(models.Model):
    CAS = models.CharField(max_length=32)
    chinese_name = models.CharField(max_length=32)
    english_name = models.CharField(max_length=32)
    details = models.TextField(max_length=32)

    def __unicode__(self):  # 定义unicode函数,是为了让对象在实例化的时候,可以返回打印输出它的名字<阿文>.不至于显示为<** object>
        return "%s(%s)" % (self.chinese_name, self.english_name)