from django.urls import path
from .views import PostList, Login, Logout, SignUpView, VerifyEmailView, CreatePost, comment, UpdatePost, DeletePost, MyPage, UpdateUser, DeleteUser

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('comment/<int:post_id>', comment, name='comment'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('verify/<int:user_pk>/<str:token>/', VerifyEmailView.as_view(), name='verify'),
    path('create_post/', CreatePost.as_view(), name='create_post'),
    path('update_post/<int:pk>/', UpdatePost.as_view(), name='update_post'),
    path('delete_post/<int:pk>/', DeletePost.as_view(), name='delete_post'),
    path('my_page/<int:pk>/', MyPage.as_view(), name='my_page'),
    path('update_user/<int:pk>/', UpdateUser.as_view(), name='update_user'),
    path('delete_user/<int:pk>/', DeleteUser.as_view(), name='delete_user'),
]