from django.shortcuts import render ,redirect
from .models import Post ,User
from django.views.generic import (ListView,DetailView,
                                  CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.core.mail import send_mail,BadHeaderError
from .forms import ContactForm
from django.http import HttpResponse
from django.contrib import messages



# Create your views here.

#Creating home view
def home(request):
   posts = Post.objects.all()
   return render(request,'blog/index.html',{'posts':posts})


def get_user_profile(request,username):
    user = User.objects.get(username=username)
    return render(request,'blog/user_profile.html',{'user':user })

class PostListView(ListView):
   model = Post
   template_name = 'blog/index.html'
   context_object_name = 'posts'
   ordering = ['-date_posted']
   paginate_by = 5



class PostDetailView(DetailView):
   model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    context = {
        'posts': Post.objects.all().order_by('-date_posted')
    }

    return render(request, 'blog/about.html', context)

def contact_us (request):
    if request.method =='GET':
        form = ContactForm()
    else:
        form= ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject,message,from_email,['amdavy12@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            messages.success(request, 'Your message has been sent!')
            return redirect('blog-home')
            #return render(request, 'blog/contact_us_success.html', {'title': 'contact_us_success'})


    return render(request , 'blog/contact_us.html', {'form':form})

def contact_us_success(request):
    return render(request,'blog/contact_us_success.html',{'title':'contact_us_success'})
