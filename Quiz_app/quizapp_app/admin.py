from django.contrib import admin
from .models import quizapp,userdetail,result

@admin.register(quizapp)
class quizappAdmin(admin.ModelAdmin):
    list_display=['question']

@admin.register(userdetail)
class userdetailAdmin(admin.ModelAdmin):
    list_display=['username','email']


@admin.register(result)
class resultAdmin(admin.ModelAdmin):
    list_display=['question']
