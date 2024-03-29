from django.shortcuts import render
from .serializers import FlightSerializer, ReservationSerializer, StaffFlightSerializer
from .models import Flight, Passenger, Reservation
from rest_framework import viewsets
from .permissions import IsStafforReadOnly
from datetime import datetime, date


class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsStafforReadOnly, )

    def get_serializer_class(self):
        serializer = super().get_serializer_class()
        if self.request.user.is_staff:
            return StaffFlightSerializer
        return serializer

    def get_queryset(self):
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        today = date.today()
        query = self.request.query_params.get('keyword')
        print('query:', query)

        if self.request.user.is_staff:
            return super().get_queryset()
        else:
            queryset = Flight.objects.filter(date_of_departure__gt=now)
            if Flight.objects.filter(date_of_departure=today):
                today_qs = Flight.objects.filter(date_of_departure=today).filter(etd__gt=current_time)
                queryset = queryset.union(today_qs)
            return queryset



class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


    def get_queryset(self):
        queryset = Reservation.objects.all() # same with second one!
        # queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user=self.request.user.id)
        


