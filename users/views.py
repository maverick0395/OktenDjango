import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class UsersListCreateView(APIView):
    def get(self, request):
        try:
            with open('users.json') as file:
                data = json.load(file)
                return Response(data)

        except FileNotFoundError:
            return Response('File not found')


        except Exception as err:
            return Response(err)



    def post(self, request):
        data = self.request.data

        try:
            with open('users.json') as read_file:
                list_obj = json.load(read_file)

            list_obj.append(data)

            with open('users.json', 'w') as write_file:
                json.dump(list_obj, write_file)
                return Response('Created')

        except FileNotFoundError:
            return Response('File not found')


        except Exception as err:
            return Response(err)






