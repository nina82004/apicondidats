from django.shortcuts import render
from rest_framework import generics
from .models import Candidate, Recruiter
from .serializers import CandidateSerializer, RecruiterSerializer

# Endpoint pour gérer les candidats
class CandidateListCreateView(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class CandidateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

# Endpoint pour gérer les recruteurs
class RecruiterListCreateView(generics.ListCreateAPIView):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer

class RecruiterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer
