from django.shortcuts import render
from rest_framework import generics
from rest_framework.serializers import Serializer

from .models import Documents, Folders, SubFolders
from .serializers import DocumentSerializer, FolderSerializer, SubFolderSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
from django.urls import reverse_lazy


# Create your views here.

class FolderListView(generics.ListAPIView):
    queryset = Folders.objects.all()
    serializer_class = FolderSerializer
    
class FolderCreateView(generics.ListCreateAPIView):
    queryset = Folders.objects.all()
    serializer_class = FolderSerializer
    
    def post(self, request, *args, **kwargs):

      folder_serializer = FolderSerializer(data=request.data)

      if folder_serializer.is_valid():
          folder_serializer.save()
          return Response(folder_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(folder_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
class FolderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Folders.objects.all()
    serializer_class = FolderSerializer
    
class FolderDeleteView(generics.DestroyAPIView):
    queryset = Folders.objects.all()
    serializer_class = FolderSerializer
    
class FolderTrashView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Folders.objects.all()
    serializer_class = FolderSerializer
    
    def foldertrash(request, pk):
        doc = Folders.objects.get(id=pk)
        doc.trash = True
        doc.save()
        return redirect('folders')
    
class SubFoldersListView(generics.ListAPIView):
    queryset = SubFolders.objects.all()
    serializer_class = SubFolderSerializer
    
class SubFoldersCreateView(generics.ListCreateAPIView):
    queryset = SubFolders.objects.all()
    serializer_class = SubFolderSerializer
    
class SubFoldersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubFolders.objects.all()
    serializer_class = SubFolderSerializer
    
class DocumentListView(generics.ListAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentSerializer
    
class DocumentCreateView(generics.ListCreateAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentSerializer
    
    def DocumentCreate(request):
        if request.method == 'POST':
            serializer = DocumentSerializer(request.POST,request.FILES)
            if serializer.is_valid():
            
                serializer.save()
            return Response({'success': 'Document created successfully'}, status= status.HTTP_200_OK)
        else:
            return redirect('document-create')
        
class DocumentDetailView(generics.RetrieveUpdateAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentSerializer
    
class DocumentUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentSerializer
    
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.pk})
    
class DocumentDeleteView(generics.DestroyAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentSerializer

        
