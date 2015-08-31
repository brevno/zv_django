from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='students'),
    url(r'^courses/$', views.CoursesView.as_view(), name='courses'),
    url(r'^add_student/$', views.AddStudentView.as_view(), name='add_student'),
    url(r'^delete_student/(?P<pk>[0-9]+)/$', views.DeleteStudentView.as_view(), name='delete_student'),
    url(r'^add_course/$', views.AddCourseView.as_view(), name='add_course'),
    url(r'^delete_course/(?P<pk>[0-9]+)/$', views.DeleteCourseView.as_view(), name='delete_course'),
    url(r'^edit_rates/(?P<student_id>[0-9]+)/$', views.EditRatesView.as_view(), name='edit_rates'),
]
