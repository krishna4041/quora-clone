from django.views import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.template import loader
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,CreateView,RedirectView,UpdateView
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from quoraapp.Forms import *
from quoraapp.Forms.auth import *
from quoraapp.Forms.commentform import *
from quoraapp.Forms.questionForm import *
from quoraapp.Forms.answerform import *
from quoraapp.models import *
from django.urls import reverse_lazy

class FeedView(LoginRequiredMixin,ListView):
    login_url = "/login/"
    model=Question
    context_object_name='feed_list'
    template_name='feed.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        # import ipdb
        # ipdb.set_trace()
        context = super(FeedView, self).get_context_data(**kwargs)
        data=self.model.objects.values('id','question_by','question_title')
        #context['headings'] = list(data[0].keys())
        context['feed'] = data
        return context

class CreateQuestionView(LoginRequiredMixin,CreateView):
    # import ipdb
    # ipdb.set_trace()
    login_url = "/login/"
    model = Question
    form_class = Questionform
    template_name = 'addquestion.html'
    success_url = reverse_lazy('feed_view')
    def form_valid(self, form):
        # import ipdb
        # ipdb.set_trace()
        form.instance.question_by = self.request.user.username
        form.instance.user_id=self.request.user.id
        return super().form_valid(form)


#8008494843

class CreateAnswerView(LoginRequiredMixin,CreateView):
    # import ipdb
    # ipdb.set_trace()
    login_url = "/login/"
    model = Answer
    form_class = Answerform
    template_name = 'addanswer.html'

    def post(self, request, *args, **kwargs):
        # import ipdb
        # ipdb.set_trace()
        answer_form = Answerform(request.POST)

        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.for_question_id=kwargs['id']
            answer.answer_by=request.user.username
            # student.college = college
            answer.save()
            return redirect('/Question/{0}/'.format(kwargs['id']))


class CreateCommentView(LoginRequiredMixin,CreateView):
    # import ipdb
    # ipdb.set_trace()
    login_url = "/login/"
    model = Comment
    form_class = Commentform
    template_name = 'addcomment.html'

    def post(self, request, *args, **kwargs):
        # import ipdb
        # ipdb.set_trace()
        comment_form = Commentform(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.for_comment_id=kwargs['id']
            Answer.objects.values().filter(id=kwargs['id']).update(for_flag=1)
            comment.comment_by=request.user.username
            # student.college = college
            comment.save()
            return redirect('/Question/{0}/'.format(kwargs['great']))



class SingleQuestionView(LoginRequiredMixin,View):
    login_url = "/login/"

    def get_by_acronym(request,id):
        question=Question.objects.values('id','question_title').filter(id=id)
        answers=Answer.objects.values().filter(for_question_id=id)
        comments=Comment.objects.all()
        templalte=loader.get_template('SingleAnswerQuestion.html')
        context=dict()
        context['comments']=comments
        context['question']=question
        context['answer_list']=answers
        return HttpResponse(templalte.render(context,request))

class Upvote(LoginRequiredMixin,View):
    login_url = "/login/"

    def get_upvote(request,great,id):
        # import ipdb
        # ipdb.set_trace()
        answer=Answer.objects.get(id=id)
        answer.upvote=answer.upvote+1
        answer.save()
        return redirect('/Question/{0}/'.format(great))

class BookmarkAnswer(LoginRequiredMixin,View):
    login_url = "/login/"

    def Book(request,great,id):
        B=Bookmark(answer_id=id,user_id=request.user.id)
        B.save()
        return redirect('/Question/{0}/'.format(great))

class MybookMarks(LoginRequiredMixin,View):
    login_url = "/login/"
    def get_book_marks(request):
        point=0
        # import ipdb
        # ipdb.set_trace()
        bookmarks=Bookmark.objects.values().filter(user_id=request.user.id)
        if len(bookmarks)==0:
            data=None
        else:
            for i in bookmarks:
                get=Question.objects.values().filter(id=i['answer_id'])
                if get:
                    if point==0:
                        data=get
                        point=1
                    else:
                        data=data | get
            # import ipdb
        # ipdb.set_trace()
        templalte = loader.get_template('BookMarks.html')
        context=dict()
        context['answer']=data
        point=0
        return HttpResponse(templalte.render(context, request))

class DisplayUserinfo(LoginRequiredMixin,ListView):
    login_url = "/login/"
    model = User
    template_name = "userdetails.html"
    def get_context_data(self, **kwargs):
        # import ipdb
        # ipdb.set_trace()
        context = super(DisplayUserinfo, self).get_context_data(**kwargs)
        user_info=self.model.objects.values().filter(id=self.request.user.id)
        context['user_info']=user_info
        return context


def UserDetails(request):
    # import ipdb
    # ipdb.set_trace()
    user=User.objects.values('id','first_name','last_name','email','username').filter(id=request.user.id)
    templalte = loader.get_template('userdetails.html')
    context=dict()
    context['user']=user
    return HttpResponse(templalte.render(context, request))


class UserDetailsUpdate(LoginRequiredMixin,UpdateView):
    login_url = "/login/"
    model = User
   # fields = ['first_name','last_name','email','username']
    form_class = EditUserProfileForm
    template_name = 'edituserdetails.html'
    success_url = reverse_lazy('info')

    def get_object(self, queryset=None):
        return get_object_or_404(User,id=self.kwargs['id'])



