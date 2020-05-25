from django.shortcuts import render, redirect, HttpResponse
from .models import Organisation
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from django.views.generic.edit import FormMixin
from .forms import OrganisationForm, AuthUserForm, RegisterUserForm, CommentForm
from django.urls import reverse, reverse_lazy 
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

# Create your views here.
class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)

class HomeListView(ListView):
    model = Organisation
    template_name = 'index.html'
    context_object_name = 'list_organisation'

class HomeDetailView(CustomSuccessMessageMixin, FormMixin, DetailView):
    model = Organisation
    template_name = 'detail.html'
    context_object_name = 'get_organisation'
    form_class = CommentForm
    success_msg = 'Комментарий успешно создан, ожидайте модерации'

    def get_success_url(self, **kwargs):
        return reverse_lazy('detail_page', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.organisation = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)




class OrganisationCreateView(LoginRequiredMixin, CustomSuccessMessageMixin, CreateView):
    model = Organisation
    template_name = 'edit_page.html'
    form_class = OrganisationForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись создана'
    def get_context_data(self, **kwargs):
        kwargs['list_organisation'] = Organisation.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class OrganisationUpdateView(LoginRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = Organisation
    template_name = 'edit_page.html'
    form_class = OrganisationForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись успешно обновлена'

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user !=  kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs

class OrganisationDeleteView(LoginRequiredMixin, DeleteView):
    model = Organisation
    template_name = 'edit_page.html'
    success_url = reverse_lazy('edit_page')
    success_msg = "Запись успешно удалена"

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)
        
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.author:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

class MyprojectLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('edit_page')

    def get_success_url(self):
        return self.success_url

class RegisterUserView(CreateView):
    model = User
    template_name = 'register_page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('edit_page')
    success_msg = "Пользователь успешно создана"

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid

class MyprojectLogout(LogoutView):
    next_page = reverse_lazy('edit_page')