from django.contrib import admin
from core import models

class CurrentConditionInline(admin.TabularInline):
    model = models.CurrentCondition
    extra = 0

class OfferedConditionInline(admin.TabularInline):
    model = models.OfferedCondition
    extra = 0

class InterviewInline(admin.TabularInline):
    model = models.Interview
    extra = 0



@admin.register(models.Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ["id", "actual_company", "recruitment_company", "role"]
    inlines = [CurrentConditionInline, OfferedConditionInline, InterviewInline]


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "location", "recruitment_company"]
    list_filter = ["recruitment_company"]


@admin.register(models.ConditionType)
class ConditionTypeAdmin(admin.ModelAdmin):
    ...