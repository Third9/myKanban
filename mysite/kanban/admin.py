from django.contrib import admin

# Register your models here.
from kanban.models import Board, List, Card

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_num', 
                    'title', 'master_user', 
                    'group_user', 'create_date',
                    'modify_date')

class ListAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_num', 
                    'title', 'master_user', 
                    'group_user', 'create_date',
                    'modify_date', 'board_id')

class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_num', 
                    'title', 'info',
                    'tag', 'master_user', 
                    'group_user', 'create_date',
                    'modify_date', 'list_id', 'board_id')

admin.site.register(Board, BoardAdmin)
admin.site.register(List, ListAdmin)
admin.site.register(Card, CardAdmin)
