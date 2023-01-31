from datetime import datetime

from django.views.generic import TemplateView, ListView,DetailView
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
