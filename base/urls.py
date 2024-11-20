from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='home'),
    path('login', views.signin, name="login"),
    path('logout', views.signout, name="logout"),
    path('register', views.register, name="register"),
    path('playlist/<int:course_id>', views.playlist, name="playlist"),
    path('playlist', views.playlist, name="playlist2"),
    path('save_course', views.save_course, name='save_course'),
    path('video/<int:id>', views.watch_video, name="watch-video"),
    path('delete_comment/<int:id>', views.delete_comment, name="delete_comment"),
    path('like_video/<int:id>', views.like_video, name="like_video"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('courses', views.courses, name="courses"),
    path('tutors', views.tutors, name="tutors"),
    path('profile', views.profile, name="profile"),
    path('teacher/<int:id>', views.teacher_profile, name="teacher_profile"),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('liked_videos/', views.liked_videos, name='liked_videos'),
    path('user_comments/', views.user_comments, name='user_comments'),
    path('tutor/dashboard/', views.tutor_dashboard, name='tutor_dashboard'),
    path('tutor/courses/add/', views.add_course, name='add_course'),
    path('tutor/courses/', views.my_courses, name='my_courses'),
    path('tutor/courses/<int:course_id>/edit/', views.edit_course, name='edit_course'),
    path('tutor/courses/<int:course_id>/delete/', views.delete_course, name='delete_course'),
    path('tutor/students/', views.students_list, name='students_list'),
    path('tutor/analytics/', views.analytics, name='analytics'),
    path('tutor/student/<int:student_id>/course/<int:course_id>/', 
         views.student_progress, name='student_progress'),
]