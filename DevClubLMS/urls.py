"""DevClubLMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.contrib.auth import views as auth_views
from grades import views as grade_views
from grades.views import GradeCreateView,GradeDetailView,GradeUpdateView,GradeDeleteView
# from users.views import CourseDetailView
from communication.views import AnnListView,AnnDetailView,AnnCreateView,AnnUpdateView,AnnDeleteView,UserAnnListView
from courses_available.views import CourseListView,CourseDetailView,CourseCreateView,CourseUpdateView,CourseDeleteView
from documents.views import DocListView,DocDetailView,DocCreateView,DocUpdateView,DocDeleteView,UserDocListView
# from grades.views import GradeListView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',user_views.home,name='home-page'),
    path('courses/',user_views.allCourses,name='allCourses-page'),
    path('register/',user_views.register,name='register'),
    path('',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/',user_views.profile,name='profile'),
    # path('profile/<str:username>',user_views.profile, name='profile'),
    # path('courses/<int:pk>/',CourseDetailView.as_view(),name='course-detail'),
    path('announcements/',AnnListView.as_view(),name='announcements'),
    path('announcements/<int:pk>/',AnnDetailView.as_view(),name='announcement-detail'),
    path('announcements/new/',AnnCreateView.as_view(),name='announcement-create'),
    path('announcements/<int:pk>/update/',AnnUpdateView.as_view(),name='announcement-update'),
    path('announcements/<int:pk>/delete/',AnnDeleteView.as_view(),name='announcement-delete'),
    path('announcements/<str:username>/',UserAnnListView.as_view(),name='user-announcement'),
    path('documents/',DocListView.as_view(),name='documents'),
    path('documents/<int:pk>/',DocDetailView.as_view(),name='document-detail'),
    path('documents/new/',DocCreateView.as_view(),name='document-create'),
    path('documents/<int:pk>/update/',DocUpdateView.as_view(),name='document-update'),
    path('documents/<int:pk>/delete/',DocDeleteView.as_view(),name='document-delete'),
    path('documents/<str:username>/',UserDocListView.as_view(),name='user-document'),
    path('grades/',grade_views.index,name='grades'),
    path('grades/new/',GradeCreateView.as_view(),name='grade-create'),
    path('grades/<int:pk>/',GradeDetailView.as_view(),name='grade-detail'),
    path('grades/<int:pk>/update/',GradeUpdateView.as_view(),name='grade-update'),
    path('grades/<int:pk>/delete/',GradeDeleteView.as_view(),name='grade-delete'),
    path('allCourses/',CourseListView.as_view(),name='courses-available'),
    path('courses/<int:pk>/',CourseDetailView.as_view(),name='course-detail'),
    path('courses/new/',CourseCreateView.as_view(),name='course-create'),
    path('courses/<int:pk>/update/',CourseUpdateView.as_view(),name='course-update'),
    path('courses/<int:pk>/delete/',CourseDeleteView.as_view(),name='course-delete')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# path('grades/', grade_views.index)
# path('coursepage/',user_views.coursePage,name='course-page'),

# app/model_viewtype.html
#communication/announcement_list.html
