from rest_framework import serializers

from .models import Documents, Folders, SubFolders

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folders
        fields = ['name']
        
class SubFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubFolders
        fields = ['name','folders']
        
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = ['title','uploaded_by','upload_file','image','description']