from django.urls import re_path
from . import views

app_name = 'posts'

urlpatterns = [
    re_path(r'^$',views.PostList.as_view(),name='all'),
    re_path(r'^new/$',views.CreatePost.as_view(),name='create'),
    re_path(r'^by/(?P<username>[-\w]+)/$',views.UserPosts.as_view(),name="for_user"),
    re_path(r'by/(?P<username>[-\w]+)/(?P<pk>\d+)/$',views.PostDetail.as_view(),name="single"),
    re_path(r'^delete/(?P<pk>\d+)/$',views.DeletePost.as_view(),name='delete'),

    re_path(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment_to_post'),
    re_path(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
]
