from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.utils import timezone

# Create your views here.
from django.views.generic import ListView, DetailView, FormView, DeleteView, CreateView, UpdateView
from django.views.generic.edit import FormMixin
from braces.views import LoginRequiredMixin, UserFormKwargsMixin

from cookiecutter_practice.itemrequest.models import ItemRequest
from cookiecutter_practice.itemrequest.forms import ItemRequestForm, ItemRequestUpdateForm

class RequestList(ListView):
    model = ItemRequest

    def get_context_data(self, **kwargs):
        context = super(RequestList, self).get_context_data(**kwargs)
        if self.request.user.is_superuser:
            context["saved_requests"] = \
                ItemRequest.objects.filter(state__in=["1"])
            context["submitted_requests"] = \
                ItemRequest.objects.filter(state__in=["2"])
            context["approved_requests"] = \
                ItemRequest.objects.filter(state__in=["4"])
        else:
            context["saved_requests"] = \
                ItemRequest.objects.filter(created_by=self.request.user).filter(state__in=["1"])
            context["submitted_requests"] = \
                ItemRequest.objects.filter(created_by=self.request.user).filter(state__in=["2"])
            context["approved_requests"] = \
                ItemRequest.objects.filter(created_by=self.request.user).filter(state__in=["4"])
            
        return context

class RequestDetail(DetailView):
    model = ItemRequest

    def get_context_data(self, **kwargs):
        context = super(RequestDetail, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class RequestFormView(UserFormKwargsMixin, FormView):
    template_name = 'itemrequest/itemrequest_form.html' 
    form_class = ItemRequestForm
    success_url = '/'

    def form_valid(self, form):
        form = form.save(commit=False)
        if 'save' in self.request.POST:
            form.state = 1
        elif 'submit' in self.request.POST:
            form.state = 2
        else:
            form.state = 0
        form.created_by = self.request.user  # use your own profile here
        form.save()

        return super(RequestFormView, self).form_valid(form)

# form = RequestFormView()

class RequestUpdateView(UpdateView):
    model = ItemRequest
    template_name = 'itemrequest/itemrequest_update.html'
    form_class = ItemRequestUpdateForm

    # def get_success_url(self):
    #     success_url = reverse('request-detail', kwargs={'pk': self.pk})

    # def form_valid(self, form):
    #     form = form.save(commit=False)
        
    #     if 'save' in self.request.POST:
    #         form.state = 1
    #     elif 'submit' in self.request.POST:
    #         form.state = 2
    #     else:
    #         form.state = 0
    #     form.save()
    #     return super(RequestUpdateView, self).form_valid(form)

class RequestDeleteView(DeleteView):
    model = ItemRequest
    success_url = "/requests/"