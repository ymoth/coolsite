from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .api import WomenAPI, UserAPI
from .views import *


# WomenHome.as_view()


async def slider(request: HttpRequest) -> str:
    return render(request, 'women/slider.html')


async def test(request: HttpRequest) -> str:
    return render(request, 'women/test.html')


urlpatterns = [
    path('', WomenHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
    path('slider/', slider, name='slider'),
    path('test/', test, name='test'),
    path('api/v1/womenlist', WomenAPI.as_view()),
    path('api/v1/userlist', UserAPI.as_view()),
]
