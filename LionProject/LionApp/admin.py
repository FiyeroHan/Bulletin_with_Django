from django.contrib import admin
from .models import Post,Reple
# Register your models here.
admin.site.register(Post)
admin.site.register(Reple)


'''
마이그레이션 명렁어 (DB 수정할때 쓰는거)
python3 manage.py makemigrations
python3 manage.py migrate
'''