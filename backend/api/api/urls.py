"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views.admin import admin_list, admin_detail, admin_login
from .views.learner import create_learner, learner_details, learner_login, register_for_course, get_learners_courses
from .views.courses import course_list, course_detail, course_material_list, course_material_detail
from .views.course_materials import create_course_material, get_course_material
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
       openapi.Info(
                 title="e_teach API",
                 default_version='v1',
                 description="online learning api",
                 terms_of_service="https://www.google.com/policies/terms/",
                 contact=openapi.Contact(email="contact@snippets.local"),
                 license=openapi.License(name="BSD License"),
              ),
       public=True,
       permission_classes=(permissions.AllowAny,),
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admins', admin_list),
    path('admins/<int:id>', admin_detail),
    path('admins/login', admin_login),
    path('learners', create_learner),
    path('learners/courses', get_learners_courses),
    path('learners/register/<int:cid>', register_for_course),
    path('learners/<int:id>', learner_details),
    path('learners/login', learner_login),
    path('courses', course_list),
    path('courses/<int:cid>/materials/<int:cmid>', course_material_detail),
    path('courses/<int:id>/materials', course_material_list),
    path('courses/<int:id>', course_detail),
    path('course_materials', create_course_material),
    path('course_materials/<int:id>', get_course_material),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
