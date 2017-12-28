from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
#Username (leave blank to use 'yanji'): root
#Email address: 907231602@qq.com
#Password:18408671831yjj

@python_2_unicode_compatible   #兼容python2.x和python3.x
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')

    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.title


