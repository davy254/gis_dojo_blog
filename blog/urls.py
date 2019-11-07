from django.urls import path
from . import views
from .views import  PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView



urlpatterns = [
    path('user/profile/<username>/', views.get_user_profile,name='user-profile'),
    path('' , PostListView.as_view() , name = 'blog-home'),
    path('posts/<int:pk>/' , PostDetailView.as_view() , name = 'post-detail'),
    path('posts/<int:pk>/delete/' , PostDeleteView.as_view() , name = 'post-delete'),
    path('posts/<int:pk>/update/' , PostUpdateView.as_view() , name = 'post-update'),
    path('posts/new/' , PostCreateView.as_view() , name = 'post-create'),
    path('about/', views.about , name = 'blog-about'),
    path('contact-us/', views.contact_us, name="blog-contact-us"),
    path('contact-us-success/', views.contact_us_success, name="blog-contact-us-success")

]