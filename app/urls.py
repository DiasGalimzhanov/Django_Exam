from django.urls import path
from .views import PostList, Login, Logout, SignUpView, VerifyEmailView, CreatePost,  home, comment

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('comment/<int:post_id>', comment, name='comment'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('verify/<int:user_pk>/<str:token>/', VerifyEmailView.as_view(), name='verify'),
    path('create_post/', CreatePost.as_view(), name='create_post'),
]