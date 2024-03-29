from django.urls import path

from petstagram.main.views.generic import HomeView, DashboardView
from petstagram.main.views.pet_photos import CreatePetPhotoView, PetPhotoDetailsView, like_pet_photo, EditPetPhotoView
from petstagram.main.views.pets import CreatePetView, EditPetView, DeletePetView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('pet/create/', CreatePetView.as_view(), name='create pet'),
    path('pet/edit/<int:pk>/', EditPetView.as_view(), name='edit pet'),
    path('pet/delete/<int:pk>/', DeletePetView.as_view(), name='delete pet'),

    path('photo/add/', CreatePetPhotoView.as_view(), name='create photo'),
    path('photo/edit/<int:pk>/', EditPetPhotoView.as_view(), name='edit photo'),
    path('photo/details/<int:pk>/', PetPhotoDetailsView.as_view(), name='pet photo details'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo')
)
