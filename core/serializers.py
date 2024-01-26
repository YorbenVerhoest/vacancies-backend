from rest_framework import serializers
from core import models


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ['id', 'name', 'recruitment_company','location']


class ConditionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ConditionType
        fields = ['name']

class ConditionSerializer(serializers.ModelSerializer):
    condition_type = ConditionTypeSerializer()
    
    class Meta:
        model = models.CurrentCondition
        fields = ['condition_type', 'value','bool_value']


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Interview
        fields = ['datetime', 'interview_type']


class VacancySerializer(serializers.ModelSerializer):
    actual_company = CompanySerializer()
    recruitment_company = CompanySerializer()
    current_conditions = serializers.SerializerMethodField()
    offered_conditions = serializers.SerializerMethodField()
    interviews = serializers.SerializerMethodField()
    
    class Meta:
        model = models.Vacancy
        fields = ['id', 'actual_company', 'recruitment_company','role','link', 'current_conditions', 'offered_conditions', 'interviews']

    def get_current_conditions(self,instance):
        currentconditions = ConditionSerializer(instance.currentcondition_set.all(), many=True).data
        return list(currentconditions)

    def get_offered_conditions(self,instance):
        offeredconditions = ConditionSerializer(instance.offeredcondition_set.all(), many=True).data
        return list(offeredconditions)
    
    def get_interviews(self,instance):
        interviews = InterviewSerializer(instance.interview_set.all(), many=True).data
        return list(interviews)


class VacancyShortSerializer(serializers.ModelSerializer):
    actual_company = CompanySerializer()
    recruitment_company = CompanySerializer()
    current_conditions = serializers.SerializerMethodField()
    offered_conditions = serializers.SerializerMethodField()
    
    class Meta:
        model = models.Vacancy
        fields = ['id', 'actual_company', 'recruitment_company','role','link', 'current_conditions', 'offered_conditions']

    def get_current_conditions(self,instance):
        currentconditions = ConditionSerializer(instance.currentcondition_set.all(), many=True).data
        return list(currentconditions)

    def get_offered_conditions(self,instance):
        offeredconditions = ConditionSerializer(instance.offeredcondition_set.all(), many=True).data
        return list(offeredconditions)
    


class InterviewSerializer(serializers.ModelSerializer):
    from_vacancy = VacancyShortSerializer()
    datetime = serializers.SerializerMethodField()

    class Meta:
        model = models.Interview
        fields = ['datetime', 'interview_type', 'from_vacancy']

    def get_datetime(self, obj):
        return obj.datetime.strftime('%d/%m/%Y - %H:%M')
