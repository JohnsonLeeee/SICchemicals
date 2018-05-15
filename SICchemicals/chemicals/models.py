from django.db import models

# Create your models here# .

PUBLIC_OR_PRIVATE_CHOICES = (
    ("0", u"公用"),
    ("1", u"私有")
)


class Person(models.Model):
    name = models.CharField(u"姓名", unique=True, max_length=32)
    contact = models.CharField(u"联系方式", null=True, max_length=32, blank=True)

    class Meta:
        verbose_name = u"人员"
        verbose_name_plural = verbose_name
        ordering = ["name"]

    def __str__(self):
        return self.name


class Student(Person):
    class Meta:
        verbose_name = u"学生"
        verbose_name_plural = verbose_name
        ordering = ["name"]


class Staff(Person):
    class Meta:
        verbose_name = u"老师/职工"
        verbose_name_plural = verbose_name
        ordering = ["id"]


class ChemicalsMessage(models.Model):
    CAS = models.CharField(u"CAS号", unique=True, max_length=32)
    chinese_name = models.CharField(u"中文名称", max_length=64, blank=True)  # 如有别名，请用逗号分隔
    english_name = models.CharField(u"英文名称", null=True, max_length=64, blank=True)    # 如有别名，请用逗号分隔
    chemical_formula = models.CharField(u"化学式", null=True, max_length=64, blank=True)   # 如有别名，请用逗号分隔
    details = models.TextField(u"详细信息", null=True, blank=True)         # 比如存储方式，易燃易爆，有无毒害，等

    class Meta:
        verbose_name = u"药品信息"
        verbose_name_plural = verbose_name
        ordering = ["id"]

    def __str__(self):
        return self.chinese_name


class Location(models.Model):
    location = models.CharField(u"存储位置", unique=True, null=False, max_length=32)
    responsible_man = models.ForeignKey(Person, verbose_name=u"柜子负责人", null=True, blank=True)
    details = models.TextField(u"详细信息", null=True, blank=True)      # 柜子的性质

    class Meta:
        verbose_name = u"位置信息"
        verbose_name_plural = verbose_name
        ordering = ["id"]

    def __str__(self):
        return self.location


class Chemical(models.Model):
    CAS = models.ForeignKey(ChemicalsMessage)
    size = models.CharField(u"规格", null=True, max_length=32, blank=True)
    number = models.IntegerField(u"数量", default=1)
    public_or_private = models.CharField(u"公用/私人", choices=PUBLIC_OR_PRIVATE_CHOICES, default="0", max_length=4)
    location = models.ForeignKey(Location, verbose_name=u"存储位置", null=True, blank=True)
    entry_time = models.DateField(u"入库时间", auto_now_add=True)
    purchaser = models.ForeignKey(Person, verbose_name=u"购买人", related_name="purchaser", null=True, blank=True)
    approver = models.ForeignKey(Staff, verbose_name=u"审批人", related_name="approver", null=True, blank=True)
    responsible_man = models.ForeignKey(Person, verbose_name=u"负责人",
                                        related_name="responsible_man", null=True, blank=True)

    class Meta:
        verbose_name = u"药品列表"
        verbose_name_plural = verbose_name
        ordering = ["id"]

    def __str__(self):
        return self.CAS.chinese_name + " " + self.CAS.chemical_formula







