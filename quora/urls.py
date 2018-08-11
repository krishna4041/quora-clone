"""quora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from quoraapp.Views.auth import *
from quoraapp.Views.questionView import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("logout/",Logout_user  ),
    path('Question/<int:id>/',SingleQuestionView.get_by_acronym),
    path('signup/', SignupView.as_view()),
    path('login/', Login_user.as_view(),name='login'),
    path('feed/',FeedView.as_view(),name='feed_view'),
    path('addQuestion/',CreateQuestionView.as_view()),
    path('addAnswer/<int:id>/',CreateAnswerView.as_view()),
    path('addComment/<int:great>/<int:id>/',CreateCommentView.as_view()),
    path('upvote/<int:great>/<int:id>/',Upvote.get_upvote),
    path('addBookmark/<int:great>/<int:id>/',BookmarkAnswer.Book),
    path('showBookmarks/',MybookMarks.get_book_marks),
    path('user_info/',UserDetails,name='info'),
    path('editprofile/<int:id>/',UserDetailsUpdate.as_view(),name='info'),
]

if settings.DEBUG :
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)