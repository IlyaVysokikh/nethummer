from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status

class BaseAPIView(APIView):
    """
    Базовый класс CRUD
    """

    model = None
    serializer_class = None


    def get_instance(self, id):
        try:    
            return self.model.objects.get(id=id)
        except:
            return None
    
    def get(self, request, id):
        instance = self.get_instance(id)
        
        if not instance:
            return Response({
                'status': 'fail',
                'message': f'Курс с id = {id} не найден'
            },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(instance)

        return Response({
            'status': 'success',
            f'{self.model._meta.model_name}': serializer.data
        },
            status=status.HTTP_200_OK
        )
    def put(self, request, id):
        instance = self.get_instance(id)
        if not instance:
            return Response({
                'status': 'fail',
                'message': f'Курс с id = {id} не найден'
            },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                f'{self.model._meta.__name__}': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'status': 'fail',
            'message': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        instance = self.get_instance(id)

        if not instance:
            return Response({
                'status': 'fail',
                'message': f'Курс с id = {id} не найден'
            },
                status=status.HTTP_404_NOT_FOUND
            )

        instance.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    

class BaseListAPIView(ListAPIView):
    model = None
    serializer_class = None

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                f'{self.model._meta.__name__}': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'fail',
            'message': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

