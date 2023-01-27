from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Product, File
from .serializers import CategorySerializer, ProductSerializer, FileSerializer


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context={'request': request}) #when you run server, you want to have full path (absolute adrress) to the file (from http (full url) not from /media/) => add context argument
        return Response(serializer.data)


class CategoryDetailView(APIView):
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, context={'request': request})
        return Response(serializer.data)



class ProductListView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': request}) #when you run server, you want to have full path (absolute adrress) to the file (from http (full url) not from /media/) => add context argument
        return Response(serializer.data)


class ProductDetailView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)


class FileListView(APIView):
    #here we only give id of product
    def get(self, request, product_id): #it takes id of one product and returns the list of files for that product
        files = File.objects.filter(product_id=product_id)
        serializer = FileSerializer(files, many=True, context={'request': request}) #when you run server, you want to have full path (absolute adrress) to the file (from http (full url) not from /media/) => add context argument
        return Response(serializer.data)


#here we give id of both product and file
class FileDetailView(APIView):
    def get(self, request, product_id, pk):
        try:
            f = File.objects.get(pk=pk, product_id=product_id)
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = FileSerializer(f, context={'request': request})
        return Response(serializer.data)
