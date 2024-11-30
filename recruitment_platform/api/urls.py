
from django.urls import path
from .views import CandidateListCreateView, CandidateDetailView, RecruiterListCreateView, RecruiterDetailView

urlpatterns = [
    path('candidates/', CandidateListCreateView.as_view(), name='candidate-list-create'),
    path('candidates/<int:pk>/', CandidateDetailView.as_view(), name='candidate-detail'),
    path('recruiters/', RecruiterListCreateView.as_view(), name='recruiter-list-create'),
    path('recruiters/<int:pk>/', RecruiterDetailView.as_view(), name='recruiter-detail'),
]