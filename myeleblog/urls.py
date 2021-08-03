from django.urls import path
from django.urls.resolvers import URLPattern

from . import views
 
urlpatterns = [
   path('',views.HomeView.as_view(),name='home'),
    path('post/<int:pk>',views.Post_Detail_view.as_view(),name='detail_view'),
    path('add_post',views.Add_Post.as_view(),name='add_post'),
    path('post/edit/<int:pk>',views.UpdatePostview.as_view(),name='post_edit'),
    path('post/delete/<int:pk>',views.DeletePostView.as_view(),name='post_delete'),
    
    path('like/<int:pk>/',views.LikeView,name='like_post'),
    
]