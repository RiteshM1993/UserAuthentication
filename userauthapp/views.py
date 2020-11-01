from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.views import APIView
from userdetails.models import ValidUser,InValidUser
from django.contrib.auth.models import User

class LoginApiView(APIView):

    http_method_names = ['post']

    permission_classes = [AllowAny,]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            queryset = InValidUser(user_name=request.data.get("username"), message="Invalid Credentials or Not a valid user")
            queryset.save()
            return Response({'error': 'Invalid Credentials or Not a valid user'},
                            status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        user_queryset = User.objects.get(username=request.data.get("username"))
        queryset = ValidUser(user_name=user_queryset,message="Valid User")
        queryset.save()
        return Response({'token': token.key},
                        status=HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
def hello_world_api(request):
    data = {'data': "Hello World Api"}
    return Response(data, status=HTTP_200_OK)