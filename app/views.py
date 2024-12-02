from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog

class BlogListView(ListView):
    model = Blog
    template_name = 'blog.html'  
    context_object_name = 'blogs'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'single-blog.html'
    context_object_name = 'blog'

def home_view(request):
    return render(request, "index.html")

def about_view(request):
    return render(request, "about.html")

def contact_view(request):
    return render(request, "contact.html")

def portfolio_view(request):
    return render(request, "portfolio.html")

def single_portfolio_view(request):
    return render(request, "single-portfolio.html")

# class PortfolioListView(ListView):
#     model = Portfolio
#     context_object_name = 'portfolios'
#     template_name = "portfolio.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["categories"] = PortfolioCategory.objects.all()
#         return context

# def portfolio_view(request):
#     portfolio = Portfolio.objects.all()

#     context = {
        
#         "portfoios":portfolio,
#     }
#     return render(request,'portfolio.html', context)
