from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
#from rest_framework.permissions import
from rest_framework import status
import firebase_admin
from firebase_admin import auth
from firebase_admin import functions

class SendWelcomeEmailView(APIView):

    def post(self, request):
        email = request.data.get('email')
        name = request.data.get('name')

        if not email or not name:
            return Response({'error': 'Email and name are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Call the Firebase function
        try:
            send_welcome_email = firebase_admin.functions.function('sendWelcomeEmail')
            result = send_welcome_email({'email': email, 'name': name})
            return Response({'success': True, 'result': result}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
