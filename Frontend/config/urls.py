from django.contrib import admin
from django.urls import path
from my_app.views import submit_fraud_report  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', submit_fraud_report, name='home'), 
]