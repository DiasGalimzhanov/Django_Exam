from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import redirect
from .forms import SignUpForm, LoginForm, PostCreateForm
from .models import CustomUser, Post, Comment
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin 
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


def comment(request, post_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            author = CustomUser.objects.get(id=request.user.id)
            text = request.POST.get('text')
            post1 = Post.objects.get(id=post_id)
            Comment.objects.create(author=author, text=text, post=post1)
            return redirect('comment', post_id)
    else:
        return redirect('login')
    post = Post.objects.get(id=post_id)
    return render(request, 'comment.html', {'post_id': post ,'post': post.comments.all()})


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'home.html'
    paginate_by = 5

class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    login_url = reverse_lazy('login')
    template_name = 'create_post.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class MyPage(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'my_page.html'
    context_object_name = 'user'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(author=self.request.user)
        return context

class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    login_url = reverse_lazy('login')
    template_name = 'update_post.html'
    fields = ['content', 'image']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    login_url = reverse_lazy('login')
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class SignUpView(SuccessMessageMixin, CreateView):
    model = CustomUser
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    success_message = 'Account created successfully'
    
    def send_verification_email(self, user):
        token = default_token_generator.make_token(user)
        verify_url = self.request.build_absolute_uri(f'/verify/{user.pk}/{token}/')
        subject = 'Verify your email'
        message = f'Hello {user.username}, please click the link below to verify your email:\n\n{verify_url}'
        send_mail(subject, message, 'dias199770@gmail.com', [user.email])

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object  
        user.is_active = False
        user.save()
        self.send_verification_email(self.object)
        return response
    
class VerifyEmailView(View):
    def get(self, request, user_pk, token):
        user = CustomUser.objects.get(pk=user_pk)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Your email has been verified')
            return redirect('login')
        else:
            messages.error(request, 'Invalid verification link')
            return redirect('home')

class Login(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    #form_class = LoginForm
    next_page = reverse_lazy('home')
    success_message = 'You are logged in successfully'
    
class Logout(LogoutView):
    next_page = reverse_lazy('home')

class UpdateUser(LoginRequiredMixin, UpdateView):
    model = CustomUser
    login_url = reverse_lazy('login')
    template_name = 'update_user.html'
    fields = ['username', 'email', 'image', 'first_name', 'last_name']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeleteUser(LoginRequiredMixin, DeleteView):
    model = CustomUser
    login_url = reverse_lazy('login')
    template_name = 'delete_user.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

