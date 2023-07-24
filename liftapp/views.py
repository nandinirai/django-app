import json
from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.core import serializers
from .models import Elevator, Request


class ElevatorView(View):

    def get(self, request,elevator_id=None):
        req= str(request)
        if elevator_id is None:
            elevators = Elevator.objects.all()
        else:
            elevators = Elevator.objects.filter(id=elevator_id)
            if req.find("next_destination") != -1:
                return HttpResponse(elevators.values('direction'))
            elif req.find("is_moving") != -1:
                return HttpResponse(elevators.values('is_available'))
            elif req.find("door") != -1:
                return HttpResponse(elevators.values('is_door_open'))

        return HttpResponse(elevators.values())

    def post(self, request, elevator_id):

        if elevator_id is None:
            return HttpResponse("Invalid elevator ID.")

        request_data = request.POST
        floor = request_data["floor"]
        direction = request_data["direction"]

        request = Request(elevator_id=elevator_id, floor=floor, direction=direction)
        request.save()

        return HttpResponse("Request saved successfully.")


class RequestView(View):

    def get(self, request, elevator_id):     
        if elevator_id is None:
            Request.objects.all()
            return HttpResponse("Invalid elevator ID.")
        
        requests = Request.objects.filter(elevator_id=elevator_id)
        return HttpResponse(requests)
    
    def post(self, request, elevator_id):

        if elevator_id is None:
            return HttpResponse("Invalid elevator ID.")

        request_data = request.POST
        print(json.dumps(request_data))

        floor = request_data["floor"]
        direction = request_data["direction"]

        request = Request.objects.create(elevator_id=Elevator.objects.get(id=elevator_id), 
                                         floor=floor, 
                                         direction=direction)
        request.save()

        return HttpResponse("Request saved successfully.")

