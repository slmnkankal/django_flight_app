from django.shortcuts import render
from .serializers import FlightSerializer, ReservationSerializer
from .models import Flight, Passenger, Reservation
from rest_framework import viewsets
from .permissions import IsStafforReadOnly



class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsStafforReadOnly, )



class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


    def get_queryset(self):
        # queryset = Reservation.objects.all() # same with second one!
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user=self.request.user)
        


