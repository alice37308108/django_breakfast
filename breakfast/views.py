from datetime import datetime

from django.contrib.auth import login
from django.core.checks import messages
from django.shortcuts import resolve_url

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import BreakfastModelForm, SignupForm, LoginForm
from .models import Breakfast, Tag

from django.shortcuts import render
from django.views.decorators.http import require_POST


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignupForm()

    param = {
        'form': form
    }

    return render(request, 'breakfast/signup.html', param)


def login_view(request):  # ユーザーのログイン
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()

            if user:
                login(request,user)
    else:
        form = LoginForm()

    # コンテキスト変数を含めたparamの作成
    index_view = IndexView()
    index_context = index_view.get_context_data()
    param = {
        'form': form,
        **index_context,
    }
    return render(request, 'breakfast/login.html', param)

def logout_view(request):  # ユーザーのログアウト
    pass


def user_view(request):  # ログインユーザーの情報の表示
    pass


def other_view(request):  # 他のユーザーの情報の表示
    pass


class IndexView(TemplateView):
    template_name = 'breakfast/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.now().strftime('%Y/%m/%d %H:%M')
        now_hour = datetime.now().hour
        if 5 <= now_hour < 10:
            context['message'] = 'おはようございます'
        elif 10 <= now_hour < 18:
            context['message'] = 'こんにちは'
        else:
            context['message'] = 'こんばんは'
        return context


class BreakfastListView(ListView):
    model = Breakfast
    template_name = 'breakfast/list.html'
    context_object_name = 'breakfast_list'
    paginate_by = 5

    def get_queryset(self):
        qs = Breakfast.objects.order_by('-date')
        search_query = self.request.GET.get('search')
        feeling_query = self.request.GET.get('feeling')
        if search_query and feeling_query:
            qs = qs.filter(breakfast__icontains=search_query, feeling__exact=feeling_query)
        elif search_query:
            qs = qs.filter(breakfast__icontains=search_query)
        elif feeling_query:
            qs = qs.filter(feeling__exact=feeling_query)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.kwargs.get('tag')
        if context['tag']:
            context['tag_queryset'] = Tag.objects.filter(slug=context['tag'])
        else:
            context['tag_queryset'] = Tag.objects.all()
        return context


class ItemDetailView(DetailView):
    model = Breakfast
    template_name = 'breakfast/detail.html'
    context_object_name = 'breakfast'

    def get_queryset(self):
        return Breakfast.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BreakfastCreateView(CreateView):
    template_name = 'breakfast/form.html'
    form_class = BreakfastModelForm
    success_url = reverse_lazy('breakfast:list')


# 成功した時に実行される処理
# def get_success_url(self):
#     messages.success(self.request, '登録しました。')
#     return resolve_url('breakfast:list')


class BreakfastUpdateView(UpdateView):
    template_name = 'breakfast/form.html'
    model = Breakfast
    form_class = BreakfastModelForm
    success_url = reverse_lazy('breakfast:list')

    def get_queryset(self):
        return Breakfast.objects.all()

    def form_valid(self, form):
        messages.success(self.request, '更新しました。')
        return super().form_valid(form)

    def get_success_url(self):
        return resolve_url('breakfast:detail', pk=self.kwargs['pk'])


class BreakfastDeleteView(DeleteView):
    template_name = 'breakfast/delete.html'
    model = Breakfast
    success_url = reverse_lazy('breakfast:list')

    def get_queryset(self):
        return Breakfast.objects.all()

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, '削除しました。')
        return super().delete(request, *args, **kwargs)


class ContactListView(ListView):
    model = Breakfast
    template_name = 'breakfast/page_list.html'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
