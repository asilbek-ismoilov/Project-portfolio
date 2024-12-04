from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import IndexView, AboutView, BlogListView, BlogDetailView,  ContactFormView, PortfolioListView, PortfolioDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='home-page'),
    path('about/',AboutView.as_view(),name='about-page'),
    path('blog/',BlogListView.as_view(),name='blog-page'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog-detail'),
    path('contact/', ContactFormView.as_view(), name='contact-page'),
    path('portfolio/', PortfolioListView.as_view(), name='portfolio-page'),
    path('portfolio/<slug:slug>/', PortfolioDetailView.as_view(), name='portfolio-detail'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)