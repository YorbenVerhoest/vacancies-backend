from django.db import models
from model_utils import Choices



INTERVIEW_TYPE = Choices(
    ('INTAKE', ('Intake')),
    ('FOLLOWUP', ('Follow-up')),
    ('COMPANY', ('Company')),
)


class Company(models.Model):
    name = models.CharField(max_length=200)
    recruitment_company = models.BooleanField()
    location = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    actual_company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True, related_name="company")
    recruitment_company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True, related_name="recruiting_company")
    role = models.CharField(max_length=200)
    link = models.URLField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        # return f"{self.actual_company.name if self.actual_company else self.recruitment_company.name} - {self.role}"
        return f"{self.pk}"
    
    def save(self, *args, **kwargs):
        try:
            if self.currentcondition_set.filter(condition_type_id=1).count() == 0:
                self.currentcondition_set.create(condition_type_id=1, value="2550")
            if self.currentcondition_set.filter(condition_type_id=7).count() == 0:
                self.currentcondition_set.create(condition_type_id=7, bool_value=True)
            if self.currentcondition_set.filter(condition_type_id=8).count() == 0:
                self.currentcondition_set.create(condition_type_id=8, bool_value=True)
            if self.currentcondition_set.filter(condition_type_id=3).count() == 0:
                self.currentcondition_set.create(condition_type_id=3, value="2,34")
        except:
            ...
        super().save(*args, **kwargs)



class Interview(models.Model):
    from_vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    interview_type = models.CharField(max_length=50, choices=INTERVIEW_TYPE)


class ConditionType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class AbstractCondition(models.Model):
    from_vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    condition_type = models.ForeignKey(ConditionType, on_delete=models.CASCADE)
    value = models.CharField(max_length=200, blank=True, null=True)
    bool_value = models.BooleanField(blank=True, null=True)

    class Meta:
        abstract = True

class CurrentCondition(AbstractCondition):
    ...


class OfferedCondition(AbstractCondition):
    ...

