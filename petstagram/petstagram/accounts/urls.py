from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from petstagram.accounts.views import UserLoginView, UserRegisterView, ProfileDetailView, EditProfileView, \
    ChangeUserPasswordView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit-password/', ChangeUserPasswordView.as_view(), name='change password'),
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile details'),
    path('create/', UserRegisterView.as_view(), name='create profile'),
    path('edit/', EditProfileView.as_view(), name='edit profile'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('dashboard')), name='password_change_done')
    # path('profile/delete/', delete_profile, name='delete profile'),
)
