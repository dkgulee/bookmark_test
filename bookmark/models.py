from django.db import models

# Create your models here. site 이름 url need



class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        return self.site_name + " : " + self.url


# admin 파일에 등록을 해야 관리자 페이지에 적용이 된다.

