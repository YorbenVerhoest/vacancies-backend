from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import api

app_name = 'core'

# router = routers.SimpleRouter()
router = DefaultRouter()
router.register(r'vacancy', api.VacancyViewset, basename="Vacancy")
router.register(r'company', api.CompanyViewset, basename="Company")
router.register(r'latest', api.LatestInterview, basename="Latest-interview")
router.register(r'upcomming', api.UpcommingInterview, basename="Upcomming-interview")

# entity_logo_link_router = routers.NestedSimpleRouter(router, r'establishments', lookup='establishment')
# entity_logo_link_router.register(r'logolink', entity_links.EstablishmentLogoLinkViewset, basename="EstablishmentLogoLinkViewset")

urlpatterns = [
    path('api/', include(router.urls)),

]
