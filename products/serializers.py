from rest_framework import serializers

from .models import Category, Product, File

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'description', 'avatar')


class FileSerializer(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField()
    class Meta:
        model = File
        fields = ('id', 'title', 'file', 'file_type')
#I included id then program will return id as well, when I call FileList in the url.

    def get_file_type(self, obj):
        return obj.get_file_type_display()

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True) #because it is manytomany (it is more than one)
    files = FileSerializer(many=True) #many is True since it moght be more than one (this is to show the detail)
#Product has a categories field which has manytomany relationship with Category
#without above line it only shows ids. but with this line we get the details of product with the categories
#for the files: we want to have file in the json respose as well as product and category => add file to the next class and to get the file details, add files to the above class. also add related_name='files' to models.py -> File (foreignKey line)

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'avatar', 'categories', 'files', 'url')

#min: 8:50:54  if you want to add a field (to show in the browser) which is not n the model: 1-add it to the above fileds 2- make the following method3- add the 3rd line to ProductSerializer


