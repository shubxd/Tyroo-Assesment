from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.utils import IntegrityError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class RegisterUser(APIView):
    """
        signup api
    """
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        try:
            user = User(username=username)
            user.set_password(password)
            user.save()

            return Response(
                {"status": "success"}
            )
        except IntegrityError:
            return Response({"status": f"username already exists"})
        except Exception as e:
            return Response({"message": f"could not create user as {e}"})


class LogoutView(APIView):
    """
        logout api
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

