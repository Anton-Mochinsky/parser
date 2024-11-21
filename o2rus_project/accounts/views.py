from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import RegisterSerializer, UserSerializer
import requests
from rest_framework.permissions import IsAuthenticated
from .models import SearchHistory
from .serializers import SearchHistorySerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class PartSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, part_number):
        # Пример интеграции с внешними сайтами
        external_sites = [
            "https://example-parts-site.com/api/search",
            "https://another-parts-site.com/api/search",
        ]
        
        search_results = []
        
        for site in external_sites:
            try:
                response = requests.get(f"{site}?part_number={part_number}")
                if response.status_code == 200:
                    data = response.json()
                    search_results.extend(data.get('results', []))
            except Exception as e:
                search_results.append({'error': f"Failed to fetch from {site}: {str(e)}"})

        # Сохраняем результаты поиска
        history = SearchHistory.objects.create(
            user=request.user,
            part_number=part_number,
            results=search_results
        )

        return Response({
            "part_number": part_number,
            "results": search_results
        })

