from django.urls import path, re_path
from suggestionbox import views

#app_name = AppName

urlpatterns = [
    path('',views.CreatePostView.as_view(),name='create_post'),
    path(r'^post/publish/$',views.post_publish,name='post_publish'),
    path('thankyou/',views.DoneView.as_view(),name='thankyou'),
]