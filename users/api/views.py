from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from users.api.serializers import RegistrationSerializer


@api_view(['GET', ])
@permission_classes([AllowAny])
def user_api_links(request):
    data = {
        'register': 'user/api/register/'
    }

    return Response(data)


@api_view(['POST', ])
@permission_classes([AllowAny])
def register(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}

    if serializer.is_valid():
        user = serializer.save()

        data['phone_number'] = user.phone_number
        token = Token.objects.get(user=user).key
        data['token'] = token

    else:
        data = serializer.errors

    return Response(data)
