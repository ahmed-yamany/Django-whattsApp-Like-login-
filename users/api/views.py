from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from users.api.serializers import (
    RegistrationSerializer,
    CodeSerializer
)
from users.models import FamTamUser
from codes.models import Code


@api_view(['GET', ])
@permission_classes([AllowAny])
def user_api_links(request):
    data = {
        'register-or-login': 'user/api/register_or_login/',

    }

    return Response(data)


@api_view(['POST', ])
@permission_classes([AllowAny])
def register_or_login(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    try:
        phone_number = request.POST['phone_number']
    except:
        phone_number = '00000000000'
    if serializer.is_valid():

        serializer.save()
        data['message'] = 'We create a new account for you, Thanks for join us'

        data['phone_number'] = serializer.data['phone_number']

        # send code message

    elif FamTamUser.objects.filter(phone_number=phone_number).exists():
        user = FamTamUser.objects.get(phone_number=phone_number)
        code = user.code
        data['message'] = 'you have an account'
        code.save()  # change user code when login

        # send code message


    else:
        data['errors'] = serializer.errors

    return Response(data)


@api_view(['POST', ])
@permission_classes([AllowAny])
def verify_code(request):
    serializer = CodeSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        phone_number = serializer.data['phone_number']
        code = serializer.data['code']
        user = FamTamUser.objects.get(phone_number=phone_number)
        if str(code) == str(user.code):
            token = Token.objects.get(user=user).key

            data['token'] = token
        else:
            data['error'] = 'Invalid or Expired code'

    else:
        data['errors'] = serializer.errors

    return Response(data)
