from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog, Portfolio, PortfolioCategory
from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ContactForm

class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/"  # Redirect to home page upon successful form submission

    def form_valid(self, form):
        form.save()  # Save the form data to the database
        return super().form_valid(form)

    def form_invalid(self, form):
        # Set 'placeholder' to 'xato' for invalid fields
        for field in form.errors:
            form.fields[field].widget.attrs['placeholder'] = "xato"
        return self.render_to_response(self.get_context_data(form=form))

class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'portfolio.html'
    context_object_name = 'portfolios'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = PortfolioCategory.objects.all()
        return context

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'single-portfolio.html'
    context_object_name = 'portfolio'

    
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