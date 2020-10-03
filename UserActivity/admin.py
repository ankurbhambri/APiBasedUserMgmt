from django.contrib import admin
from UserActivity.models import UserProfile, UsersActivity


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'start_time', 'end_time', 'time_zone',)
    search_fields = ('id', 'full_name',)


@admin.register(UsersActivity)
class UsersActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'extra_feild',)
    search_fields = ('id', 'extra_feild',)
