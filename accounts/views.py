from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerializer

# Create your views here.
class UserRegistrationView(APIView):
    """
     Register the User with post request.

     Also checks for the User's type (doctor or patient).
    """

    def post(request):
        data=request.data.copy()
        user_type=data.get('user_type')

        if user_type == 'doctor':
            data['is_doctor']=True
        elif user_type == 'patient':
            data['is_patient']=True
        else:
            return Response({'error':'Invalid User Type'},status=status.HTTP_400_BAD_REQUEST)
        
        serializer= UserRegisterSerializer(data)
        if serializer.is_valid():
            user= serializer.save()
            return Response({
                'message': f'{user_type.capitalize()} registered successfully.',
                'unique_id': user.unique_id
            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)