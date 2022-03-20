from django.urls import path


from .views import start_page, whoami, source_code, random

app_name = 'hillel_hw_8'

urlpatterns = [
    path('', start_page),
    path('whoami/', whoami),
    path('source_code/', source_code),
    path('random/', random),
]
