# from django.shortcuts import render, redirect
from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.main.forms import CreatePetForm, EditPetForm, DeletePetForm


# from petstagram.main.helpers import get_profile
# from petstagram.main.models import Pet


# def pet_action(request, form_class, success_url, instance, template_name):
#     if request.method == 'POST':
#         form = form_class(request.POST, instance=instance)
#         if form.is_valid():
#             form.save()
#             return redirect(success_url)
#     else:
#         form = form_class(instance=instance)
#     context = {
#         'form': form,
#         'pet': instance
#     }
#     return render(request, template_name, context)


class CreatePetView(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'main/pet_create.html'
    form_class = CreatePetForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user == self.request.user
        return context


class EditPetView(views.UpdateView):
    template_name = 'main/pet_edit.html'
    form_class = EditPetForm


class DeletePetView(views.DeleteView):
    template_name = 'main/pet_delete.html'
    form_class = DeletePetForm

# def create_pet(request):
#     return pet_action(request, CreatePetForm, 'profile details', Pet(user_profile=get_profile()),
#                       'main/pet_create.html')
#
#
# def edit_pet(request, pk):
#     return pet_action(request, EditPetForm, 'profile details', Pet.objects.get(pk=pk), 'main/pet_edit.html')
#
#
# def delete_pet(request, pk):
#     return pet_action(request, DeletePetForm, 'profile details', Pet.objects.get(pk=pk), 'main/pet_delete.html')
