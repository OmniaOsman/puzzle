from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .serializers import GetPuzzleSerializer, PostPuzzleSerializer
from .tasks import solve_puzzle
from .models import Puzzle
from rest_framework.generics import RetrieveAPIView, ListAPIView


class GetPuzzleAPIView(APIView):
    serializer_class = GetPuzzleSerializer

    def get_serializer(self, *args, **kwargs):
        # A method to get an instance of the serializer class
        return self.serializer_class(*args, **kwargs)

    def get(self, request, id=None):
        if id is not None:
            puzzle = get_object_or_404(Puzzle, id=id)
        else:
            puzzle = Puzzle.objects.all()

        # Serialize the puzzle object or queryset into JSON format
        serializer = self.get_serializer(puzzle, many=id is None)
        return Response(serializer.data, status=200)



class PostPuzzleApiView(APIView):
    serializer_class = PostPuzzleSerializer
    
    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            data    = serializer.validated_data['data']
            level   = serializer.validated_data['level']
            task = solve_puzzle.apply_async((data, level))
            task_id = task.id

            return Response({'task_id': task_id}, status=201)
        
        else:
            return Response(serializer.errors, status=400)

