from django.conf.urls import url

urlpatterns = [
    url(r'^', 'pysa.views.system', name='System'),
]
