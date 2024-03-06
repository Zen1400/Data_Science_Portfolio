from django.contrib import admin

from . models import (
    UserProfile,
    Media,
    Portfolio,
    Skill
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'user')       # display the fields that you want in the admin page

# @admin.register(ContactProfile)
# class ContactAdmin(admin.ModelAdmin):
# 	list_display = ('id', 'timestamp', 'name',)

# @admin.register(Testimonial)
# class TestimonialAdmin(admin.ModelAdmin):
#     list_display = ('id','name','is_active')

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id','projects')


# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ('id','name','is_active')
#     readonly_fields = ('slug',)

# @admin.register(Education)
# class EducationAdmin(admin.ModelAdmin):
#     list_display = ('id','name')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id','name')
