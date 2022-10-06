from typing_extensions import Required
from rest_framework import serializers
from .models import Flight, Passenger, Reservation

class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = (
            "id",
            "flight_number",
            "operation_airlines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "etd"
        )


class PassengerSerializer(serializers.ModelSerializer):
    pas_id = serializers.IntegerField(source='id', required=False)
    class Meta:
        model = Passenger
        fields = (
            "id",
            "pas_id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
        )

class ReservationSerializer(serializers.ModelSerializer):

    passenger = PassengerSerializer(many=True, required=False)
    flight = serializers.StringRelatedField(read_only=False)   #default read_only=True
    user = serializers.StringRelatedField()     #default read_only=True
    flight_id = serializers.IntegerField(required=False)
    user_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Reservation
        fields = (
            "id",
            "flight",
            "flight_id",
            "user",
            "user_id",  # write_only
            "passenger"
        )

    def create(self, validated_data):
        passenger_data = validated_data.pop('passenger')
        print(validated_data)
        validated_data['user_id'] = self.context['request'].user.id
        reservation = Reservation.objects.create(**validated_data)
        for passenger in passenger_data:
            pas = Passenger.objects.create(**passenger)
            reservation.passenger.add(pas)
        reservation.save()
        return reservation

    def update(self, instance, validated_data):
        passenger_data = validated_data.pop('passenger')
        present = instance.passenger.all()
        
        ###########################################
        #update yapılırken yolcu silmek için (to erase passenger when updating reservation)
        
        presentIdlist=[Id.id for Id in present ]
        updatedIdlist= [item["id"] for item in passenger_data if "id" in item.keys()]
        print(presentIdlist)
        for Id in presentIdlist:
            if Id in updatedIdlist:
                pass
            else:
                print("non exist", Id)
                present = present.exclude(id=Id)
        instance.passenger.set(present)
        print("present : ", present[0].id)
        #######################################
        
        for passenger in passenger_data:
            try:
                pas = present.filter(id=passenger["id"])
                if pas:
                    pas = pas.update(**passenger)
            except:
                pas = Passenger.objects.create(**passenger)
                instance.passenger.add(pas)
        instance.flight_id = validated_data["flight_id"]
        instance.save()
        return instance


class StaffFlightSerializer(serializers.ModelSerializer):

    reservations = ReservationSerializer(many=True, read_only=True)

    class Meta:
        model = Flight
        fields = (
            "id",
            "flight_number",
            "operation_airlines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "etd",
            "reservations"
        )



