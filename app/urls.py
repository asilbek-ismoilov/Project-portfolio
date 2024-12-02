from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home_view, about_view, BlogListView, BlogDetailView,  contact_view, portfolio_view, single_portfolio_view

urlpatterns = [
    path('', home_view, name='home-page'),
    path('about/',about_view,name='about-page'),
    path('blog/',BlogListView.as_view(),name='blog-page'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog-detail'),
    path('contact/',contact_view,name='contact-page'),
    path('portfolio/',portfolio_view,name='portfolio-page'),
    path('blog-detail/',single_portfolio_view,name='blog-detail'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)