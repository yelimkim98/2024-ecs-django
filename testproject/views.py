from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def index(request):
    data = {
        "result":"success",
        "data": [
            {
                "id": "yerimkim",
                "name": "김예림",
            },
            {
                "id": "jjongseong",
                "name": "이종성",
            },
        ]
    }
    return Response(data, status=status.HTTP_200_OK)