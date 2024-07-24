from django.contrib import admin

from about_us.models import AboutUs, GrowthHistory, Advantages, Questions


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title_about_us', 'text_about_us')


@admin.register(GrowthHistory)
class GrowthHistoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'text')
    search_fields = ('title', 'year')


@admin.register(Advantages)
class AdvantagesAdmin(admin.ModelAdmin):
    list_display = ('text',)


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
