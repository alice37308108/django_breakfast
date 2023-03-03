from datetime import datetime

from django.core.checks import messages
from django.shortcuts import resolve_url
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, FormView, UpdateView, DeleteView

from .forms import BreakfastForm, BreakfastModelForm
from .models import Breakfast


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

    def get_queryset(self):
        return Breakfast.objects.order_by('-date')


class ItemDetailView(DetailView):
    model = Breakfast
    template_name = 'breakfast/detail.html'
    context_object_name = 'breakfast'

    def get_queryset(self):
        return Breakfast.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        breakfast = self.get_object()
        # context['feelings'] = range(breakfast.feeling)
        context['feelings'] = dict(feeling='★' * breakfast.feeling + '☆' * (5 - breakfast.feeling))
        return context


class BreakfastFormView(FormView):
    form_class = BreakfastForm
    template_name = 'breakfast/form.html'
    success_url = reverse_lazy('breakfast:list')

    def form_valid(self, form):
        # form.save()
        return super().form_valid(form)


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
