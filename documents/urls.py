from django.urls import path

from .models import SubFolders
from .views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('folders/', FolderListView.as_view()),
    path('foldercreate/', FolderCreateView.as_view()),
    path('folderdetail/<slug>', FolderDetailView.as_view()),
    path('folderdelete/<int:pk>', FolderDeleteView.as_view()),
    path('foldertrash/<int:pk>', FolderTrashView.as_view()),
    
    path('subfolders/', SubFoldersListView.as_view()),
    path('subfolderscreate/', SubFoldersCreateView.as_view()),
    path('subfoldersdetail/', SubFoldersDetailView.as_view()),
    
    path('doc/', DocumentListView.as_view()),
    path('documentcreate/', DocumentCreateView.as_view(), name='document-create'),
    path('documentdetail/<int:pk>/', DocumentDetailView.as_view()),
    path('documentupdate/<int:pk>/', DocumentUpdateView.as_view()),
    path('documentdelete/<int:pk>/', DocumentDeleteView.as_view()),
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)