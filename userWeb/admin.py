from django.contrib import admin

from .models import Profile, Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'directors', 'release_date', 'genres')
    list_filter = ('regions', 'genres')
    search_fields = ('name', 'actors', 'directors')
    fieldsets = (
        ('基本信息', {
            'fields': ('name', 'alias', 'cover', 'storyline')
        }),
        ('详细信息', {
            'fields': ('actors', 'directors', 'genres', 'languages', 'mins', 'release_date')
        }),
        ('评分信息', {
            'fields': ('douban_score', 'douban_votes', 'imdb_id')
        }),
        ('其他', {
            'fields': ('official_site', 'regions'),
            'classes': ('collapse',)  # 折叠该字段集合
        })
    )


# class MovieInline(admin.TabularInline):
#     model = Movie
#     show_change_link = False


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_date_joined', 'is_first_login')
    list_filter = ('is_first_login',)
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('user', 'is_first_login')

    # inlines = [
    #     MovieInline,
    # ]

    # def has_delete_permission(self, request, obj=None):
    #     # 禁止删除Profile对象
    #     return False
    #
    # def get_actions(self, request):
    #     # 禁止在列表页进行批量操作
    #     actions = super().get_actions(request)
    #     del actions['delete_selected']
    #     return actions
    def user_date_joined(self, obj):
        return obj.user.date_joined

    user_date_joined.short_description = 'User Creation Time'
    user_date_joined.admin_order_field = 'user__date_joined'


# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Movie, MovieAdmin)
