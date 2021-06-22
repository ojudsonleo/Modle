from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index.php', index.as_view(), name='index'),
    path('ide/Graphql', graphql),
    path('ide/Python', python),
    path('', login),
    path('cloud_os/', os),
    path("WebTerminal/", word_pratice),
    path("git/", include("gitrepo.urls")),
    path("profile/", include("portfolio.urls")),
    path("register/", register.as_view()),
    path('project', include("app.urls"), name='project'),
    path('blog/', include('blog.urls')),
]
