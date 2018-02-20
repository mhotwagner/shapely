from django.conf.urls import url

from .views import ShapeViewSet

app_name = 'shapes'
urlpatterns = [
    url('shapes/', ShapeViewSet.as_view({'get': 'list'}), name='shape_list'),
]
